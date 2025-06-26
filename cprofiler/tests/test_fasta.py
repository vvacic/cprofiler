import os

from cprofiler.aminoacid import AminoAcid
from cprofiler.fasta import Fasta
from cprofiler.profile import CompositionProfiler


def test_fasta_read_count():
    """Test Fasta.read() and Fasta.count_chars()"""
    surface = CompositionProfiler.get_background_file('surface')

    assert os.path.exists(surface)

    sequences = Fasta.read(surface)

    assert len(sequences) == 633

    t = Fasta.count_chars(sequences, AminoAcid.AA_1_LETTER)

    assert t[0, 0] == 7
    assert sum(t)[0] == 6623
