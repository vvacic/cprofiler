from cprofiler.aminoacid import AminoAcid
from cprofiler.fasta import Fasta
from cprofiler.profile import CompositionProfiler


def test_discover():
    surface = CompositionProfiler.get_background_file('surface')
    pdbs25 = CompositionProfiler.get_background_file('pdbs25')

    query = Fasta.read(surface)
    background = Fasta.read(pdbs25)

    alphabet = AminoAcid.AA_ORDER['alpha']

    query_counts = Fasta.count_chars(query, alphabet)
    background_counts = Fasta.count_chars(background, alphabet)

    df = CompositionProfiler.discover(query_counts,
        background_counts,
        alphabet,
        groups = AminoAcid.AA_GROUP,
        group_names = AminoAcid.AA_GROUP_NAME,
        iterations = 10000,
        alpha_value = 0.05 / 40)

    assert abs(df.effect[0] + 0.217772) <= 1e-6
    assert abs(df.effect[20] + 0.184723) <= 1e-6

    assert df.test_result[0] == 'Depleted'
    assert df.test_result[2] == 'Enriched'
    assert df.test_result[5] == 'Not significant'


def test_relent():
    surface = CompositionProfiler.get_background_file('surface')
    pdbs25 = CompositionProfiler.get_background_file('pdbs25')

    query = Fasta.read(surface)
    background = Fasta.read(pdbs25)

    alphabet = AminoAcid.AA_ORDER['alpha']

    query_counts = Fasta.count_chars(query, alphabet)
    background_counts = Fasta.count_chars(background, alphabet)

    relent, pvalue = CompositionProfiler.relent(query_counts, background_counts)

    assert abs(relent - 0.059797352551317795) < 1e-6
    assert pvalue <= 0.0001
