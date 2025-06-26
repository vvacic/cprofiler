"""
Composition Profiler class for discovery, plotting and relative entropy

Vladimir Vacic
Algorithms and Computational Biology Lab
Department of Computer Science and Engineering
University of California, Riverside
Riverside, CA 92521, USA
"""

import importlib.resources
from importlib.resources.abc import Traversable
from pathlib import Path
from typing import Dict, ItemsView, List, Tuple

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# For reproducible results
np.random.seed(128)


class CompositionProfiler:
    """ Composition Profiler class for discovery, plotting and relative entropy """

    BACKGROUND_NAME = {
        'sprot':   'Proteins from SwissProt 51',
        'pdbs25':  'PDB Select 25',
        'surface': 'Surface residues of monomers from PDB',
        'disprot': 'Disordered regions from DisProt 3.4'
    }

    BACKGROUND_FILE = {
        'sprot':   'sprot51_5k.fa',
        'pdbs25':  'pdb_s25.fa',
        'surface': 'monomers.fa',
        'disprot': 'disprot_3.4.fa'
    }

    @staticmethod
    def list_backgrounds() -> List[str]:
        """List all background distributions"""
        return list(CompositionProfiler.BACKGROUND_NAME.keys())

    @staticmethod
    def get_background_names() -> ItemsView[str, str]:
        """Get full names for all background distributions"""

        return CompositionProfiler.BACKGROUND_NAME.items()

    @staticmethod
    def get_background_file(distribution: str) -> Traversable:
        """Return path to a background distribution FastA file"""

        return(importlib.resources.files('cprofiler.data').joinpath(
            CompositionProfiler.BACKGROUND_FILE[distribution]))


    @staticmethod
    def discover(query_counts: np.ndarray,
                 background_counts: np.ndarray,
                 alphabet: str,
                 groups: Dict[str, str],
                 group_names: Dict[str, str],
                 iterations: int = 10000,
                 alpha_value: float = 0.05) -> pd.DataFrame:
        """Looks for statistically significant composition differences between two sets"""

        # Amino acids grouped by properties
        query_groups = np.zeros((query_counts.shape[0], len(groups)))
        back_groups = np.zeros((background_counts.shape[0], len(groups)))

        aa_group_keys = list(groups.keys())
        for i in range(len(groups)):
            cols = [alphabet.index(x) for x in groups[aa_group_keys[i]]]
            query_groups[:, i] = np.sum(query_counts[:, cols], axis=1)
            back_groups[:, i] = np.sum(background_counts[:, cols], axis=1)

        # Merge
        query_counts = np.concatenate((query_counts, query_groups), axis=1)
        background_counts = np.concatenate((background_counts, back_groups), axis=1)

        # Compute fractional differences
        query_sum = np.sum(query_counts, axis=0)
        query_freq = query_sum / sum(query_sum[0:len(alphabet)])

        back_sum = np.sum(background_counts, axis=0)
        back_freq = back_sum / sum(back_sum[0:len(alphabet)])

        fracdiff = (query_freq - back_freq) / back_freq

        # Estimate significance by randomly permuting query/background labels
        query_len = len(query_counts)
        combined_counts = np.concatenate((query_counts, background_counts), axis=0)
        counts = np.zeros(len(fracdiff))

        for i in range(iterations):
            combined_counts = combined_counts[
                np.random.choice(combined_counts.shape[0],
                    combined_counts.shape[0],
                    replace=False)
                ]

            query_sum = np.sum(combined_counts[0:query_len,], axis=0)
            query_freq = query_sum / sum(query_sum[0:len(alphabet)])

            back_sum = np.sum(combined_counts[query_len+1:combined_counts.shape[0],], axis=0)
            back_freq = back_sum / sum(back_sum[0:len(alphabet)])

            tempdiff = (query_freq - back_freq) / back_freq

            # Two-tailed test
            counts += abs(tempdiff) >= abs(fracdiff)

        # Format results as data frame
        df = pd.DataFrame({
            'test_name': list(alphabet) + list(group_names.values()),
            'effect': fracdiff,
            'pvalue': counts / iterations,
            'test_result': 'Not significant'})

        df.loc[(df.pvalue < alpha_value) & (df.effect > 0), 'test_result'] = 'Enriched'
        df.loc[(df.pvalue < alpha_value) & (df.effect < 0), 'test_result'] = 'Depleted'

        return df


    @staticmethod
    def draw_barplot(residues: List[str],
                     fracdiff: np.ndarray,
                     errors: np.ndarray,
                     output_format: str,
                     output_file: str | Path,
                     colors: list[str],
                     ylab: str = '',
                     image_height: float = 5,
                     image_width: float = 3.5,
                     resolution: float = 300) -> None:
        """Wrapper for matplotlib.bar"""

        matplotlib.rcParams['font.family'] = 'sans-serif'
        matplotlib.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'Liberation Sans', 'FreeSans']
        matplotlib.rcParams['axes.spines.right'] = False
        matplotlib.rcParams['axes.spines.top'] = False

        matplotlib.use('Agg')

        plt.figure(figsize=(image_width, image_height))

        yerr_lower = np.zeros(len(fracdiff))
        yerr_upper = np.zeros(len(fracdiff))
        for i in range(len(fracdiff)):
            if fracdiff[i] >= 0:
                yerr_upper[i] = errors[i]
            if fracdiff[i] <= 0:
                yerr_lower[i] = errors[i]

        plt.bar(residues, fracdiff, color=colors)
        plt.errorbar(residues, fracdiff, yerr=[yerr_lower, yerr_upper], fmt='none',
            elinewidth=0.5, ecolor='black', capsize=5)
        plt.ylabel(ylab)
        plt.tight_layout()
        plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

        match output_format:
            case "png":
                plt.savefig(output_file, dpi=resolution)
            case "pdf" | "eps":
                plt.savefig(output_file)
        plt.close()

        return

    @staticmethod
    def plot(query_counts: np.ndarray,
             background_counts: np.ndarray,
             alphabet: str,
             reorder_by_value: bool,
             output_format: str,
             output_file: str | Path,
             colors: List[str],
             ylab: str,
             image_height: float = 3.5,
             image_width: float = 5,
             resolution: float = 300,
             iterations: int = 10000) -> None:
        """Draw a composition profile plot"""

        # Compute fractional differences
        query_sum = np.sum(query_counts, axis=0)
        query_freq = query_sum / sum(query_sum)

        back_sum = np.sum(background_counts, axis=0)
        back_freq = back_sum / sum(back_sum)

        residues = list(alphabet)
        fracdiff = (query_freq - back_freq) / back_freq

        # Estimate standard deviations via bootrap sampling
        temp = np.zeros((iterations, len(alphabet)))
        for i in range(iterations):
            query_sum = np.sum(query_counts[
                np.random.choice(query_counts.shape[0],
                    query_counts.shape[0],
                    replace=True)
                ], axis=0)
            query_freq = query_sum / sum(query_sum)

            back_sum = np.sum(background_counts[
                np.random.choice(background_counts.shape[0],
                    background_counts.shape[0],
                    replace=True)
                ], axis=0)
            back_freq = back_sum / sum(back_sum)

            temp[i,] = (query_freq - back_freq) / back_freq
        errors = np.std(temp, axis=0)

        # Sort residues according to input param value
        if reorder_by_value:
            permuted_residues = []
            permuted_fracdiff = []
            permuted_errors = []
            permuted_colors = []

            for ind in np.argsort(fracdiff):
                permuted_residues.append(residues[ind])
                permuted_fracdiff.append(fracdiff[ind])
                permuted_errors.append(errors[ind])
                permuted_colors.append(colors[ind])

            residues = permuted_residues
            fracdiff = permuted_fracdiff
            errors = permuted_errors
            colors = permuted_colors

        if output_format == 'txt':
            with open(output_file, 'w') as out:
                for i in range(len(residues)):
                    out.write(f'{residues[i]}\t{fracdiff[i]:.3f}\t{errors[i]:.3f}\n')
        else:
            CompositionProfiler.draw_barplot(residues,
                fracdiff,
                errors,
                output_format = output_format,
                output_file = output_file,
                colors = colors,
                ylab = ylab,
                image_height = image_height,
                image_width = image_width,
                resolution = resolution)

        return

    @staticmethod
    def relent(query_counts: np.ndarray,
               background_counts: np.ndarray,
               iterations: int = 10000) -> Tuple[float, float]:
        """Computes relative entropy between two distributions of residues."""

        # Compute relative entropy
        query_sum = np.sum(query_counts, axis=0)
        query_freq = query_sum / sum(query_sum)

        back_sum = np.sum(background_counts, axis=0)
        back_freq = back_sum / sum(back_sum)

        # About 3.3x faster than scipy.stats.entropy
        r = np.sum(query_freq * np.log(query_freq/back_freq))

        # Estimate significance by randomly permuting query/background labels
        query_len = len(query_counts)
        combined_counts = np.concatenate((query_counts, background_counts), axis=0)
        count = 0

        for i in range(iterations):
            combined_counts = combined_counts[
                np.random.choice(combined_counts.shape[0],
                    combined_counts.shape[0],
                    replace=False)
                ]

            query_sum = np.sum(combined_counts[0:query_len,], axis=0)
            query_freq = query_sum / sum(query_sum)

            back_sum = np.sum(combined_counts[query_len+1:combined_counts.shape[0],], axis=0)
            back_freq = back_sum / sum(back_sum)

            # One-tailed test
            if np.sum(query_freq * np.log(query_freq/back_freq)) >= r:
                count += 1

        return r, count / iterations
