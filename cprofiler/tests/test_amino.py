from cprofiler.aminoacid import AminoAcid


def test_constants():
    """Test access to AA_ORDER, AA_COLOR_SCHEME, AA_PROPERTY dicts"""

    assert AminoAcid.get_order('alpha') == 'ACDEFGHIKLMNPQRSTVWY'

    assert AminoAcid.get_color('weblogo', 'G') == '#00CC00'

    assert AminoAcid.get_property('hydrophobicity_eisenberg', 'R') == -2.53
