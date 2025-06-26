"""
Composition Profiler main CLI entry point

Vladimir Vacic
Algorithms and Computational Biology Lab
Department of Computer Science and Engineering
University of California, Riverside
Riverside, CA 92521, USA
"""

import argparse
import os
import sys

from cprofiler.aminoacid import AminoAcid
from cprofiler.fasta import Fasta
from cprofiler.profile import CompositionProfiler


def error(context: str, message: str):
    """Display error message and usage information, then exit"""

    sys.stderr.write(f"error: {message}\n")
    sys.stderr.write(f"Run cprof {context} --help to see usage information.\n")
    sys.exit(1)


def init_validate_opts():
    """Initialize and validate command line options"""

    parser = argparse.ArgumentParser(add_help=True,
        formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    #
    # Discover significant fractional differences
    #
    discover_parser = subparsers.add_parser("discover",
        formatter_class=argparse.RawTextHelpFormatter,
        help="Discover significant fractional differences")

    # Mandatory argument
    discover_parser.add_argument('-Q', dest='query_file', required=True,
        help='Query file in FastA format')

    # Mutually exclusive group for background
    back_group_1 = discover_parser.add_mutually_exclusive_group()
    back_group_1.add_argument('-B', dest='background_file',
        help='Background file in FastA format')

    distribution_names = ""
    for key, value in CompositionProfiler.get_background_names():
        distribution_names += f"{key:{12}} {value}\n"

    back_group_1.add_argument('-D', dest='distribution',
        choices=CompositionProfiler.list_backgrounds(), default='sprot',
        help='Preset background distribution. One of the following:\n\n'
             f"{distribution_names}\n"
             'Defaults to sprot.\n')

    # Optional arguments
    discover_parser.add_argument('-I', dest='iterations', type=int, default=10000,
        help='Number of bootstrap iterations. Defaults to 10,000.')

    discover_parser.add_argument('-A', dest='alpha_value', type=float, default=0.05,
        help='Significance value for statistical tests. Defaults to 0.05.')

    discover_parser.add_argument('-b', dest='bonferroni', action='store_true',
        help='Apply Bonferroni correction. Off by default.')

    #
    # Plot fractional differences
    #
    plot_parser = subparsers.add_parser("plot",
        formatter_class=argparse.RawTextHelpFormatter,
        help="Plot fractional differences")

    # Mandatory arguments
    plot_parser.add_argument('-Q', dest='query_file', required=True,
        help='Query file in FastA format')

    plot_parser.add_argument('-O', dest='output_file', required=True,
        help='Output file')

    # Mutually exclusive group for background
    back_group_2 = plot_parser.add_mutually_exclusive_group()
    back_group_2.add_argument('-B', dest='background_file',
        help='Background file in FastA format')
    back_group_2.add_argument('-D', dest='distribution',
        choices=CompositionProfiler.list_backgrounds(), default='sprot',
        help='Preset background distribution. One of the following:\n\n'
             f'{distribution_names}\n'
             'Defaults to sprot.\n')

    # Optional arguments
    plot_parser.add_argument('-I', dest='iterations', type=int, default=10000,
        help='Number of bootstrap iterations. Defaults to 10,000.')

    # Amino acid ordering
    max_length = max(len(s) for s in AminoAcid.get_order_names())
    temp = ''
    for key, value in AminoAcid.get_order_names():
        temp += f"{key:{max_length}} {value}\n"

    plot_parser.add_argument('-X', dest='aa_order',
        choices=AminoAcid.list_orders(), default='diff',
        help='Amino acid ordering. Sorts residues in the increasing order of one of the\n'
             'physicochemical or structural properties:\n\n'
             f"{temp}\n"
             'Defaults to ordering By observed differences.'
            )

    plot_parser.add_argument('-Y', dest='ylab', help='Y-axis label')

    # Color scheme
    temp = ''
    for key, value in AminoAcid.get_color_scheme_names():
        temp += f"{key:{max_length}} {value}\n"

    plot_parser.add_argument('-C', dest='color_scheme',
        choices=AminoAcid.list_color_schemes(), default='mono',
        help='Color scheme. One of the following:\n\n'
             f"{temp}\n"
             'Defaults to Monochromatic.\n')

    plot_parser.add_argument('-F', dest='output_format',
        choices=list(['png', 'pdf', 'eps', 'txt']), default='png',
        help='Output format. Defaults to png.')

    plot_parser.add_argument('-W', dest='image_width', type=float, default=5,
        help='Width of output image. Defaults to 5.')

    plot_parser.add_argument('-H', dest='image_height', type=float, default=3.5,
        help='Height of output image. Defaults to 3.5.')

    plot_parser.add_argument('-U', dest='image_size_units',
        choices=list(['inch', 'cm', 'pixel']), default='inch',
        help='Image size units. Defaults to inch.')

    plot_parser.add_argument('-R', dest='resolution', type=float, default=300,
        help='Bitmap resolution in dpi. Defaults to 300.')

    #
    # Compute relative entropy
    #
    relent_parser = subparsers.add_parser("relent",
        formatter_class=argparse.RawTextHelpFormatter,
        help="Compute relative entropy")

    # Mandatory argument
    relent_parser.add_argument('-Q', dest='query_file', required=True,
        help='Query file in FastA format')

    # Mutually exclusive group for background
    back_group_3 = relent_parser.add_mutually_exclusive_group()
    back_group_3.add_argument('-B', dest='background_file',
        help='Background file in FastA format')
    back_group_3.add_argument('-D', dest='distribution',
        choices=CompositionProfiler.list_backgrounds(), default='sprot',
        help='Preset background distribution. One of the following:\n\n'
             f"{distribution_names}\n"
             'Defaults to sprot.\n')

    # Optional argument
    relent_parser.add_argument('-I', dest='iterations', type=int, default=10000,
        help='Number of bootstrap iterations. Defaults to 10,000.')

    args = parser.parse_args()
    opts = vars(args)

    # Query sample file
    if not os.path.exists(opts['query_file']):
        error(opts['command'], f"Could not open query FastA file {opts['query_file']}.")

    if opts['background_file'] is None and opts['distribution'] is None:
        error(opts['command'], 'Either -B or -D must be selected.')

    # Background sample file
    if opts['background_file'] is not None and not os.path.exists(opts['background_file']):
        error(opts['command'], f"Could not open background FastA file {opts['background_file']}.")

    if opts['distribution'] is not None and \
        not os.path.exists(CompositionProfiler.get_background_file(opts['distribution'])):
        error(opts['command'], f"Could not open FastA file for distribution {opts['distribution']}.")

    # Number of bootstrap iterations
    if int(opts['iterations']) < 1:
        error(opts['command'], "Number of bootstrap iterations has to be a positive integer.")

    if opts['command'] == 'plot':
        if opts['image_size_units'] == "cm":
            opts['image_height'] /= 2.54
            opts['image_width'] /= 2.54
        elif opts['image_size_units'] == "pixel":
            opts['image_height'] /= opts['resolution']
            opts['image_width'] /= opts['resolution']

    return opts


def main():
    """ Composition Profiler main CLI entry point """

    opts = init_validate_opts()

    # Specify alphabet to produce data in the order in which it will be consumed
    if 'aa_order' not in opts or opts['aa_order'] not in AminoAcid.list_orders():
        alphabet = AminoAcid.get_order('alpha')
    else:
        alphabet = AminoAcid.get_order(opts['aa_order'])

    query = Fasta.read(opts['query_file'])
    query_counts = Fasta.count_chars(query, alphabet)

    if opts['background_file'] is not None:
        background = Fasta.read(opts['background_file'])
    elif opts['distribution'] is not None:
        background = Fasta.read(CompositionProfiler.get_background_file(opts['distribution']))
    background_counts = Fasta.count_chars(background, alphabet)

    if opts['command'] == 'discover':
        if opts['bonferroni']:
            opts['alpha_value'] = opts['alpha_value'] / (len(alphabet) + len(AminoAcid.get_groups()))

        df = CompositionProfiler.discover(query_counts,
            background_counts,
            alphabet = alphabet,
            groups = AminoAcid.get_groups(),
            group_names = AminoAcid.get_group_names(),
            iterations = opts['iterations'],
            alpha_value = opts['alpha_value'])
        print(df)

    if opts['command'] == 'plot':
        colors = []
        for ch in alphabet:
            colors.append(AminoAcid.get_color(opts['color_scheme'], ch))

        CompositionProfiler.plot(query_counts,
            background_counts,
            alphabet,
            reorder_by_value = (opts['aa_order'] == 'diff'),
            output_format = opts['output_format'],
            output_file = opts['output_file'],
            ylab = opts['ylab'],
            colors = colors,
            image_height = opts['image_height'],
            image_width = opts['image_width'],
            resolution = opts['resolution'],
            iterations = opts['iterations'])

    if opts['command'] == 'relent':
        relent, pvalue = CompositionProfiler.relent(query_counts,
            background_counts,
            opts['iterations'])

        print(f"Relative entropy = {relent:.3f}")
        if pvalue > 0:
            print(f"P-value = {pvalue}")
        else:
            print(f"P-value < {1 / opts['iterations']}")


if __name__ == "__main__":
    main()
