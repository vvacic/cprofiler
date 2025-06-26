"""
Functions for reading, writing and processing FastA files

Vladimir Vacic
Algorithms and Computational Biology Lab
Department of Computer Science and Engineering
University of California, Riverside
Riverside, CA 92521, USA
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, TextIO

import numpy as np


@dataclass
class Sequence:
    """Class representing a sequence with a header"""

    header: str
    sequence: str

    def count_chars(self, alphabet: str) -> np.ndarray:
        """Count occurences of each character in the alphabet in the given Sequence"""

        counts = {ch: 0 for ch in alphabet}
        for ch in self.sequence:
            if ch in alphabet:   # Silently skip unknown symbols
                counts[ch] += 1

        t = np.zeros(len(alphabet))
        for i in range(len(alphabet)):
            t[i] = counts.get(alphabet[i], 0)

        return t


class Fasta:
    """Class for reading, writing and processing FastA format files"""

    @staticmethod
    def read(filename: str):
        """Reads a FastA file and returns a list of Sequences"""

        with open(filename, "r") as fin:
            return Fasta.read_stream(fin)

    @staticmethod
    def read_stream(fin: TextIO) -> List[Sequence]:
        """Reads sequences from an open file handle"""

        sequences = []

        for line in fin:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            if line.startswith('>'):
                # New sequence header
                header = line[1:].strip()
                sequences.append(Sequence(header, ""))
            elif sequences:  # Only append sequence if we've seen a header
                sequences[-1].sequence += line

        return sequences

    @staticmethod
    def write(sequences: List[Sequence], filename: str | Path) -> None:
        """Writes sequences to a file in FastA format"""

        with open(filename, "w") as fout:
            for seq in sequences:
                fout.write(f">{seq.header}\n")

                # Split sequence into chunks of 80 characters
                for i in range(0, len(seq.sequence), 80):
                    fout.write(f"{seq.sequence[i:i+80]}\n")

                fout.write("\n")

    @staticmethod
    def count_chars(sequences: List[Sequence], alphabet: str) -> np.ndarray:
        """Count occurences of each character in the alphabet across all sequences"""

        t = np.zeros((len(sequences), len(alphabet)))

        for i in range(len(sequences)):
            t[i,] = sequences[i].count_chars(alphabet)

        return t
