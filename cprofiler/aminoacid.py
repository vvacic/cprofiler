"""
Comprehensive collection of amino acid properties and color schemes

Vladimir Vacic
Algorithms and Computational Biology Lab
Department of Computer Science and Engineering
University of California, Riverside
Riverside, CA 92521, USA
"""

from typing import Dict, ItemsView, List


class AminoAcid:
    """Comprehensive collection of amino acid properties and color schemes"""

    # 20 basic amino acid codes
    AA_1_LETTER: str = 'ACDEFGHIKLMNPQRSTVWY'
    AA_3_LETTER: List[str] = ['Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Gln', 'Glu', 'Gly', 'His', 'Ile',
                              'Leu', 'Lys', 'Met', 'Phe', 'Pro', 'Ser', 'Thr', 'Trp', 'Tyr', 'Val']

    # Mapping between 1-letter and 3-letter codes
    AA_CODE: Dict[str, str] = {
        'A': 'Ala', 'Ala': 'A',
        'C': 'Cys', 'Arg': 'R',
        'D': 'Asp', 'Asn': 'N',
        'E': 'Glu', 'Asp': 'D',
        'F': 'Phe', 'Cys': 'C',
        'G': 'Gly', 'Gln': 'Q',
        'H': 'His', 'Glu': 'E',
        'I': 'Ile', 'Gly': 'G',
        'K': 'Lys', 'His': 'H',
        'L': 'Leu', 'Ile': 'I',
        'M': 'Met', 'Leu': 'L',
        'N': 'Asn', 'Lys': 'K',
        'P': 'Pro', 'Met': 'M',
        'Q': 'Gln', 'Phe': 'F',
        'R': 'Arg', 'Pro': 'P',
        'S': 'Ser', 'Ser': 'S',
        'T': 'Thr', 'Thr': 'T',
        'V': 'Val', 'Trp': 'W',
        'W': 'Trp', 'Tyr': 'Y',
        'Y': 'Tyr', 'Val': 'V'
    }

    # Amino acids grouped by physicochemical properties
    AA_GROUP: Dict[str, str] = {
        'aromatic':                   'FWY',
        'charged':                    'KRDE',
        'pos_charged':                'KR',
        'neg_charged':                'DE',
        'hydrophobicity_eisenberg':   'PYCGAMWLVFI',
        'hydrophobicity_kyte':        'AMCFLVI',
        'hydrophobicity_fauchere':    'HTAPYVCLFIMW',
        'surface_janin':              'DEHKNPQRSTY',
        'flexibility_vihinen':        'RGQSNPDEK',
        'interface_propensity_jones': 'NRVLHCIMYFW',
        'solvation_potential_jones':  'AGSTPNRQDEK',
        'disorder_dunker':            'ARSQEGKP',
        'order_dunker':               'NCILFWYV',
        'bulkiness_zimmerman':        'ILVW',
        'polarity_zimmerman':         'KDEHR',
        'alpha_nagano':               'LKMFAHE',
        'beta_nagano':                'YCWQTLMFVI',
        'coil_nagano':                'CTDRSGYNP',
        'linker_george':              'YHTMQELFRP',
        'size_dawson':                'NETVILPQHMFKWYR'
    }

    # Names for the property groups
    AA_GROUP_NAME: Dict[str, str] = {
        'aromatic':                   'Aromatic',
        'charged':                    'Charged',
        'pos_charged':                'Positively charged',
        'neg_charged':                'Negatively charged',
        'polarity_zimmerman':         'Polar (Zimmerman)',
        'hydrophobicity_eisenberg':   'Hydrophobic (Eisenberg)',
        'hydrophobicity_kyte':        'Hydrophobic (Kyte-Doolittle)',
        'hydrophobicity_fauchere':    'Hydrophobic (Fauchere-Pliska)',
        'surface_janin':              'Exposed (Janin)',
        'flexibility_vihinen':        'Flexible (Vihinen)',
        'interface_propensity_jones': 'High interface propencity (Jones-Thornton)',
        'solvation_potential_jones':  'High solvation potenential (Jones-Thornton)',
        'alpha_nagano':               'Frequent in alpha helices (Nagano)',
        'beta_nagano':                'Frequent in beta sheets (Nagano)',
        'coil_nagano':                'Frequent in coils (Nagano)',
        'linker_george':              'High linker propensity (George-Heringa)',
        'disorder_dunker':            'Disorder promoting (Dunker)',
        'order_dunker':               'Order promoting (Dunker)',
        'bulkiness_zimmerman':        'Bulky (Zimmerman)',
        'size_dawson':                'Large (Dawson)'
    }

    # Ordering of amino acids based on physicochemical properties
    AA_ORDER: Dict[str, str] = {
        'alpha':                      'ACDEFGHIKLMNPQRSTVWY',
        'hydrophobicity_eisenberg':   'RKDQNEHSTPYCGAMWLVFI',
        'hydrophobicity_kyte':        'RKDENQHPYWSTGAMCFLVI',
        'hydrophobicity_fauchere':    'RKDENQSGHTAPYVCLFIMW',
        'surface_janin':              'KREQDNYPTHSAGWMLFVIC',
        'flexibility_vihinen':        'WCFIYVLHMATRGQSNPDEK',
        'interface_propensity_jones': 'DKSPTAEQGNRVLHCIMYFW',
        'solvation_jones':            'WFILMYVCHAGSTPNRQDEK',
        'bulkiness_zimmerman':        'GSADNCEHRQKTMPYFILVW',
        'polarity_zimmerman':         'AGILVFMCPYTSWNQKDEHR',
        'linker_george':              'CGWDINKSVAYHTMQELFRP',
        'alpha_nagano':               'YPGNSRTCIVDWQLKMFAHE',
        'beta_nagano':                'ERNPSKHDGAYCWQTLMFVI',
        'coil_nagano':                'FMLAEHIQVKWCTDRSGYNP',
        'size_dawson':                'GADCSNETVILPQHMFKWYR'
    }

    AA_ORDER_NAME: Dict[str, str] = {
        'diff':                       'By observed differences',
        'alpha':                      'Alphabetical',
        'hydrophobicity_eisenberg':   'Hydrophobicity (Eisenberg)',
        'hydrophobicity_kyte':        'Hydrophobicity (Kyte-Doolittle)',
        'hydrophobicity_fauchere':    'Hydrophobicity (Fauchere-Pliska)',
        'surface_janin':              'Surface exposure (Janin)',
        'flexibility_vihinen':        'Flexibility (Vihinen)',
        'interface_propensity_jones': 'Interface propensity (Jones-Thornton)',
        'solvation_jones':            'Solvation potential (Jones-Thornton)',
        'bulikness_zimmerman':        'Bulkiness (Zimmerman)',
        'polarity_zimmerman':         'Polarity (Zimmerman)',
        'linker_george':              'Linker propensity (George-Heringa)',
        'alpha_nagano':               'Alpha helix propensity (Nagano)',
        'beta_nagano':                'Beta structure propensity (Nagano)',
        'coil_nagano':                'Coil propensity (Nagano)',
        'size_dawson':                'Size (Dawson)'
    }

    AA_PROPERTY: Dict[str, Dict[str, float]] = {
        'hydrophobicity_eisenberg': {  # Eisenberg D, Schwarz E, Komaromy M, Wall R. (1984)
            'R': -2.53, 'K': -1.50, 'D': -0.90, 'Q': -0.85, 'N': -0.78,
            'E': -0.74, 'H': -0.40, 'S': -0.18, 'T': -0.05, 'P': 0.12,
            'Y': 0.26,  'C': 0.29,  'G': 0.48,  'A': 0.62,  'M': 0.64,
            'W': 0.81,  'L': 1.06,  'V': 1.08,  'F': 1.19,  'I': 1.38
         },
        'hydrophobicity_kyte': {  # Kyte J, Doolittle RF. (1982)
            'R': -2.53, 'K': -1.50, 'D': -0.90, 'Q': -0.85, 'N': -0.78,
            'E': -0.74, 'H': -0.40, 'S': -0.18, 'T': -0.05, 'P': 0.12,
            'Y': 0.26,  'C': 0.29,  'G': 0.48,  'A': 0.62,  'M': 0.64,
            'W': 0.81,  'L': 1.06,  'V': 1.08,  'F': 1.19,  'I': 1.38
         },
        'hydrophobicity_fauchere': {  # Fauchere JL, Pliska VE. (1983)
            'R': -1.01, 'K': -0.99, 'D': -0.77, 'E': -0.64, 'N': -0.60,
            'Q': -0.22, 'S': -0.04, 'G': 0.00,  'H': 0.13,  'T': 0.26,
            'A': 0.31,  'P': 0.72,  'Y': 0.96,  'V': 1.22,  'C': 1.54,
            'L': 1.70,  'F': 1.79,  'I': 1.80,  'M': 1.23,  'W': 2.25
         },
        'surface_janin': {  # Janin J. (1979)
            'K': -1.8,  'R': -1.4,  'E': -0.7,  'Q': -0.7,  'D': -0.6,
            'N': -0.5,  'Y': -0.4,  'P': -0.3,  'T': -0.2,  'H': -0.1,
            'S': -0.1,  'A': 0.3,   'G': 0.3,   'W': 0.3,   'M': 0.4,
            'L': 0.5,   'F': 0.5,   'V': 0.6,   'I': 0.7,   'C': 0.9
         },
        'flexibility_vihinen': {  # Vihinen M, Torkkila E. and Riikonen P. (1994)
            'W': 0.904, 'C': 0.906, 'F': 0.915, 'I': 0.927, 'Y': 0.929,
            'V': 0.931, 'L': 0.935, 'H': 0.950, 'M': 0.952, 'A': 0.984,
            'T': 0.997, 'R': 1.008, 'G': 1.031, 'Q': 1.037, 'S': 1.046,
            'N': 1.048, 'P': 1.049, 'D': 1.068, 'E': 1.094, 'K': 1.102
         },
        'interface_propensity_jones': {  # Jones and Thornton. (1996)
            'D': -0.38, 'K': -0.36, 'S': -0.33, 'P': -0.25, 'T': -0.18,
            'A': -0.17, 'E': -0.13, 'Q': -0.11, 'G': -0.07, 'N':  0.12,
            'R':  0.27, 'V':  0.27, 'L':  0.40, 'H':  0.41, 'C':  0.43,
            'I':  0.44, 'M':  0.66, 'Y':  0.66, 'F':  0.82, 'W':  0.83
         },
        'solvation_potential_jones': {  # Jones and Thornton J. (1997)
            'W': -0.68, 'F': -0.55, 'I': -0.49, 'L': -0.49, 'M': -0.40,
            'Y': -0.32, 'V': -0.31, 'C': -0.30, 'H': -0.06, 'A': 0.05,
            'G': 0.08,  'S': 0.15,  'T': 0.16,  'P': 0.19,  'N': 0.22,
            'R': 0.41,  'Q': 0.45,  'D': 0.64,  'E': 0.77,  'K': 1.61
         },
        'bulkiness_zimmerman': {
            'G': 3.4,   'S': 9.47,  'A': 11.5,  'D': 11.68, 'N': 12.82,
            'C': 13.46, 'E': 13.57, 'H': 13.69, 'R': 14.28, 'Q': 14.45,
            'K': 15.71, 'T': 15.77, 'M': 16.25, 'P': 17.43, 'Y': 18.03,
            'F': 19.8,  'I': 21.4,  'L': 21.4,  'V': 21.57, 'W': 21.67
         },
        'polarity_zimmerman':  {
            'A': 0.0,   'G': 0.0,   'I': 0.13,  'L': 0.13,  'V': 0.13,
            'F': 0.35,  'M': 1.43,  'C': 1.48,  'P': 1.58,  'Y': 1.61,
            'T': 1.66,  'S': 1.67,  'W': 2.1,   'N': 3.38,  'Q': 3.53,
            'K': 49.5,  'D': 49.7,  'E': 49.9,  'H': 51.6,  'R': 52.0
         },  # George RA, and Heringa J. (2003)
        'linker_george':  {
            'C': 0.778, 'G': 0.835, 'W': 0.895, 'D': 0.916, 'I': 0.922,
            'N': 0.944, 'K': 0.944, 'S': 0.947, 'V': 0.955, 'A': 0.964,
            'Y': 1.0,   'H': 1.014, 'T': 1.017, 'M': 1.032, 'Q': 1.047,
            'E': 1.051, 'L': 1.085, 'F': 1.119, 'R': 1.143, 'P': 1.299
         },
        'alpha_nagano':  {
            'Y': 0.63,  'P': 0.7,   'G': 0.72,  'N': 0.77,  'S': 0.78,
            'R': 0.83,  'T': 0.87,  'C': 0.94,  'I': 0.94,  'V': 0.97,
            'D': 1.0,   'W': 1.06,  'Q': 1.1,   'L': 1.23,  'K': 1.23,
            'M': 1.23,  'F': 1.23,  'A': 1.29,  'H': 1.29,  'E': 1.54
         },
        'beta_nagano':  {
            'E': 0.33,  'R': 0.67,  'N': 0.72,  'P': 0.75,  'S': 0.77,
            'K': 0.81,  'H': 0.87,  'D': 0.9,   'G': 0.9,   'A': 0.96,
            'Y': 1.07,  'C': 1.13,  'W': 1.13,  'Q': 1.18,  'T': 1.23,
            'L': 1.26,  'M': 1.29,  'F': 1.37,  'V': 1.41,  'I': 1.54
         },
        'coil_nagano':  {
            'F': 0.58,  'M': 0.62,  'L': 0.63,  'A': 0.72,  'E': 0.75,
            'H': 0.76,  'I': 0.8,   'Q': 0.81,  'V': 0.83,  'K': 0.84,
            'W': 0.87,  'C': 1.01,  'T': 1.03,  'D': 1.04,  'R': 1.33,
            'S': 1.34,  'G': 1.35,  'Y': 1.35,  'N': 1.38,  'P': 1.43
         },
        'size_dawson': {
            'G': 0.5,   'A': 2.5,   'D': 2.5,   'C': 3.0,   'S': 3.0,
            'N': 5.0,   'E': 5.0,   'T': 5.0,   'V': 5.0,   'I': 5.5,
            'L': 5.5,   'P': 5.5,   'Q': 6.0,   'H': 6.0,   'M': 6.0,
            'F': 6.5,   'K': 7.0,   'W': 7.0,   'Y': 7.0,   'R': 7.5
         }
    }

    # Define color schemes as a class attribute
    AA_COLOR_SCHEME: Dict[str, Dict[str, str]] = {
        'mono':  {
            'A': '#333333',  'C': '#333333',  'D': '#333333',  'E': '#333333',
            'F': '#333333',  'G': '#333333',  'H': '#333333',  'I': '#333333',
            'K': '#333333',  'L': '#333333',  'M': '#333333',  'N': '#333333',
            'P': '#333333',  'Q': '#333333',  'R': '#333333',  'S': '#333333',
            'T': '#333333',  'V': '#333333',  'W': '#333333',  'Y': '#333333'
        },
        'weblogo': {
            'G': '#00CC00',  'S': '#00CC00',  'T': '#00CC00',  'Y': '#00CC00',
            'C': '#00CC00',  'N': '#CC00CC',  'Q': '#CC00CC',  'K': '#0000CC',
            'R': '#0000CC',  'H': '#0000CC',  'D': '#CC0000',  'E': '#CC0000',
            'P': '#999999',  'A': '#000000',  'W': '#000000',  'F': '#000000',
            'L': '#000000',  'I': '#000000',  'M': '#000000',  'V': '#000000'
        },
        'amino': {
            'D': '#E60A0A',  'E': '#E60A0A',  'C': '#E6E600',  'M': '#E6E600',
            'K': '#145AFF',  'R': '#145AFF',  'S': '#FA9600',  'T': '#FA9600',
            'F': '#3232AA',  'Y': '#3232AA',  'N': '#00DCDC',  'Q': '#00DCDC',
            'G': '#EBEBEB',  'L': '#0F820F',  'V': '#0F820F',  'I': '#0F820F',
            'A': '#C8C8C8',  'W': '#B45AB4',  'H': '#8282D2',  'P': '#DC9682'
        },
        'shapley': {
            'D': '#A00042',  'T': '#A00042',  'E': '#660000',  'C': '#FFFF70',
            'M': '#B8A042',  'Y': '#B8A042',  'K': '#4747B8',  'R': '#00007C',
            'S': '#FF4C4C',  'Q': '#FF4C4C',  'F': '#534C42',  'P': '#534C42',
            'W': '#534C42',  'N': '#FF7C70',  'G': '#EBEBEB',  'V': '#EBEBEB',
            'I': '#004C00',  'L': '#455E45',  'A': '#8CFF8C',  'H': '#7070FF',
        },
        'aromatic': {
            'G': '#999999',  'S': '#999999',  'T': '#999999',  'Y': '#33ff33',
            'C': '#999999',  'N': '#999999',  'Q': '#999999',  'K': '#999999',
            'R': '#999999',  'H': '#999999',  'D': '#999999',  'E': '#999999',
            'P': '#999999',  'A': '#999999',  'W': '#33ff33',  'F': '#33ff33',
            'L': '#999999',  'I': '#999999',  'M': '#999999',  'V': '#999999'
        },
        'charged': {
            'G': '#999999',  'S': '#999999',  'T': '#999999',  'Y': '#999999',
            'C': '#999999',  'N': '#999999',  'Q': '#999999',  'K': '#3333ff',
            'R': '#3333ff',  'H': '#999999',  'D': '#ff3333',  'E': '#ff3333',
            'P': '#999999',  'A': '#999999',  'W': '#999999',  'F': '#999999',
            'L': '#999999',  'I': '#999999',  'M': '#999999',  'V': '#999999'
        },
        'hydrophobicity_eisenberg': {
            'P': '#333333',  'Y': '#333333',  'C': '#333333',  'G': '#333333',
            'A': '#333333',  'M': '#333333',  'W': '#333333',  'L': '#333333',
            'V': '#333333',  'F': '#333333',  'I': '#333333',  'R': '#33ffff',
            'K': '#33ffff',  'D': '#33ffff',  'Q': '#33ffff',  'N': '#33ffff',
            'E': '#33ffff',  'H': '#33ffff',  'S': '#33ffff',  'T': '#33ffff'
        },
        'hydrophobicity_kyte': {
            'A': '#333333',  'M': '#333333',  'C': '#333333',  'F': '#333333',
            'L': '#333333',  'V': '#333333',  'I': '#333333',  'R': '#33ffff',
            'K': '#33ffff',  'D': '#33ffff',  'E': '#33ffff',  'N': '#33ffff',
            'Q': '#33ffff',  'H': '#33ffff',  'P': '#33ffff',  'Y': '#33ffff',
            'W': '#33ffff',  'S': '#33ffff',  'T': '#33ffff',  'G': '#33ffff'
        },
        'hydrophobicity_fauchere': {
            'H': '#333333',  'T': '#333333',  'A': '#333333',  'P': '#333333',
            'Y': '#333333',  'V': '#333333',  'C': '#333333',  'L': '#333333',
            'F': '#333333',  'I': '#333333',  'M': '#333333',  'W': '#333333',
            'R': '#33ffff',  'K': '#33ffff',  'D': '#33ffff',  'E': '#33ffff',
            'N': '#33ffff',  'Q': '#33ffff',  'S': '#33ffff',  'G': '#33ffff'
        },
        'surface_janin': {
            'G': '#999999',  'S': '#ff8800',  'T': '#ff8800',  'Y': '#ff8800',
            'C': '#999999',  'N': '#ff8800',  'Q': '#ff8800',  'K': '#ff8800',
            'R': '#ff8800',  'H': '#ff8800',  'D': '#ff8800',  'E': '#ff8800',
            'P': '#ff8800',  'A': '#999999',  'W': '#999999',  'F': '#999999',
            'L': '#999999',  'I': '#999999',  'M': '#999999',  'V': '#999999'
        },
        'flexibility_vihinen': {
            'W': '#33ff33',  'C': '#33ff33',  'F': '#33ff33',  'I': '#33ff33',
            'Y': '#33ff33',  'V': '#33ff33',  'L': '#33ff33',  'H': '#33ff33',
            'M': '#33ff33',  'A': '#33ff33',  'T': '#33ff33',  'G': '#ff3333',
            'S': '#ff3333',  'N': '#ff3333',  'Q': '#ff3333',  'K': '#ff3333',
            'R': '#ff3333',  'D': '#ff3333',  'E': '#ff3333',  'P': '#ff3333'
        },
        'interface_propensity_jones': {
            'N': '#ff00ff',  'R': '#ff00ff',  'V': '#ff00ff',  'L': '#ff00ff',
            'H': '#ff00ff',  'C': '#ff00ff',  'I': '#ff00ff',  'M': '#ff00ff',
            'Y': '#ff00ff',  'F': '#ff00ff',  'W': '#ff00ff',  'D': '#33ffff',
            'K': '#33ffff',  'S': '#33ffff',  'P': '#33ffff',  'T': '#33ffff',
            'A': '#33ffff',  'E': '#33ffff',  'Q': '#33ffff',  'G': '#33ffff'
        },
        'solvation_jones': {
            'A': '#ff00ff',  'G': '#ff00ff',  'S': '#ff00ff',  'T': '#ff00ff',
            'P': '#ff00ff',  'N': '#ff00ff',  'R': '#ff00ff',  'Q': '#ff00ff',
            'D': '#ff00ff',  'E': '#ff00ff',  'K': '#ff00ff',  'W': '#33ffff',
            'F': '#33ffff',  'I': '#33ffff',  'L': '#33ffff',  'M': '#33ffff',
            'Y': '#33ffff',  'V': '#33ffff',  'C': '#33ffff',  'H': '#33ffff'
        },
        'disorder_dunker': {
            'G': '#ff3333',  'S': '#ff3333',  'T': '#999999',  'Y': '#3333ff',
            'C': '#3333ff',  'N': '#3333ff',  'Q': '#ff3333',  'K': '#ff3333',
            'R': '#ff3333',  'H': '#999999',  'D': '#999999',  'E': '#ff3333',
            'P': '#ff3333',  'A': '#ff3333',  'W': '#3333ff',  'F': '#3333ff',
            'L': '#3333ff',  'I': '#3333ff',  'M': '#999999',  'V': '#3333ff'
        },
        'bulkiness_zimmerman': {
            'G': '#3333ff',  'S': '#3333ff',  'A': '#3333ff',  'D': '#3333ff',
            'N': '#3333ff',  'C': '#3333ff',  'E': '#3333ff',  'H': '#3333ff',
            'R': '#3333ff',  'Q': '#3333ff',  'K': '#3333ff',  'T': '#3333ff',
            'M': '#3333ff',  'P': '#3333ff',  'Y': '#3333ff',  'F': '#3333ff',
            'I': '#ff3333',  'L': '#ff3333',  'V': '#ff3333',  'W': '#ff3333'
        },
        'polarity_zimmerman': {
            'A': '#3333ff',  'G': '#3333ff',  'I': '#3333ff',  'L': '#3333ff',
            'V': '#3333ff',  'F': '#3333ff',  'M': '#3333ff',  'C': '#3333ff',
            'P': '#3333ff',  'Y': '#3333ff',  'T': '#3333ff',  'S': '#3333ff',
            'W': '#3333ff',  'N': '#3333ff',  'Q': '#3333ff',  'K': '#ff3333',
            'D': '#ff3333',  'E': '#ff3333',  'H': '#ff3333',  'R': '#ff3333'
        },
        'linker_george': {
            'C': '#3333ff',  'G': '#3333ff',  'W': '#3333ff',  'D': '#3333ff',
            'I': '#3333ff',  'N': '#3333ff',  'K': '#3333ff',  'S': '#3333ff',
            'V': '#3333ff',  'A': '#3333ff',  'Y': '#ff3333',  'H': '#ff3333',
            'T': '#ff3333',  'M': '#ff3333',  'Q': '#ff3333',  'E': '#ff3333',
            'L': '#ff3333',  'F': '#ff3333',  'R': '#ff3333',  'P': '#ff3333'
        },
        'alpha_nagano': {
            'Y': '#3333ff',  'P': '#3333ff',  'G': '#3333ff',  'N': '#3333ff',
            'S': '#3333ff',  'R': '#3333ff',  'T': '#3333ff',  'C': '#3333ff',
            'I': '#3333ff',  'V': '#3333ff',  'D': '#3333ff',  'W': '#3333ff',
            'Q': '#3333ff',  'L': '#ff3333',  'K': '#ff3333',  'M': '#ff3333',
            'F': '#ff3333',  'A': '#ff3333',  'H': '#ff3333',  'E': '#ff3333'
        },
        'beta_nagano': {
            'E': '#3333ff',  'R': '#3333ff',  'N': '#3333ff',  'P': '#3333ff',
            'S': '#3333ff',  'K': '#3333ff',  'H': '#3333ff',  'D': '#3333ff',
            'G': '#3333ff',  'A': '#3333ff',  'Y': '#ff3333',  'C': '#ff3333',
            'W': '#ff3333',  'Q': '#ff3333',  'T': '#ff3333',  'L': '#ff3333',
            'M': '#ff3333',  'F': '#ff3333',  'V': '#ff3333',  'I': '#ff3333'
        },
        'coil_nagano': {
            'F': '#3333ff',  'M': '#3333ff',  'L': '#3333ff',  'A': '#3333ff',
            'E': '#3333ff',  'H': '#3333ff',  'I': '#3333ff',  'Q': '#3333ff',
            'V': '#3333ff',  'K': '#3333ff',  'W': '#3333ff',  'C': '#ff3333',
            'T': '#ff3333',  'D': '#ff3333',  'R': '#ff3333',  'S': '#ff3333',
            'G': '#ff3333',  'Y': '#ff3333',  'N': '#ff3333',  'P': '#ff3333'
        },
        'size_dawson': {
            'G': '#3333ff',  'A': '#3333ff',  'D': '#3333ff',  'C': '#3333ff',
            'S': '#3333ff',  'N': '#ff3333',  'E': '#ff3333',  'T': '#ff3333',
            'V': '#ff3333',  'I': '#ff3333',  'L': '#ff3333',  'P': '#ff3333',
            'Q': '#ff3333',  'H': '#ff3333',  'M': '#ff3333',  'F': '#ff3333',
            'K': '#ff3333',  'W': '#ff3333',  'Y': '#ff3333',  'R': '#ff3333'
        }
    }

    AA_COLOR_SCHEME_NAME: Dict[str, str] = {
        'mono':                       'Monochromatic',
        'weblogo':                    'Weblogo color scheme',
        'amino':                      'Amino color scheme',
        'shapley':                    'Shapley color scheme',
        'aromatic':                   'Aromatic residues',
        'charged':                    'Charged residues',
        'hydrophobicity_eisenberg':   'Hydrophobicity (Eisenberg)',
        'hydrophobicity_kyte':        'Hydrophobicity (Kyte-Doolittle)',
        'hydrophobicity_fauchere':    'Hydrophobicity (Fauchere-Pliska)',
        'surface_janin':              'Surface exposure (Janin)',
        'flexibility_vihinen':        'Flexibility (Vihinen)',
        'interface_propensity_jones': 'Interface propensity (Jones-Thornton)',
        'solvation_jones':            'Solvation potential (Jones-Thornton)',
        'disorder_dunker':            'Disorder propensity (Dunker)',
        'bulkiness_zimmerman':        'Bulkiness (Zimmerman)',
        'polarity_zimmerman':         'Polarity (Zimmerman)',
        'linker_george':              'Linker propensity (George-Heringa)',
        'alpha_nagano':               'Alpha helix propensity (Nagano)',
        'beta_nagano':                'Beta structure propensity (Nagano)',
        'coil_nagano':                'Coil propensity (Nagano)',
        'size_dawson':                'Size (Dawson)'
    }


    @staticmethod
    def is_aromatic(aa: str) -> bool:
        """Check if an amino acid is aromatic."""
        return aa in AminoAcid.AA_GROUP['aromatic']


    @staticmethod
    def is_charged(aa: str) -> bool:
        """Check if an amino acid is charged."""

        return aa in AminoAcid.AA_GROUP['charged']


    @staticmethod
    def charge(aa: str) -> int:
        """Get the charge of an amino acid"""

        if aa in AminoAcid.AA_GROUP['pos_charged']:
            return 1
        elif aa in AminoAcid.AA_GROUP['neg_charged']:
            return -1
        else:
            return 0


    @staticmethod
    def list_groups() -> List[str]:
        """Get a list of all amino acid groupings"""

        return list(AminoAcid.AA_GROUP.keys())

    @staticmethod
    def get_groups() -> Dict[str, str]:
        """Get all amino acid groupings"""

        return AminoAcid.AA_GROUP

    @staticmethod
    def get_group_names() -> Dict[str, str]:
        """Get all amino acid grouping names"""

        return AminoAcid.AA_GROUP_NAME


    @staticmethod
    def list_orders() -> List[str]:
        """Get a list of all amino acid orderings"""

        return list(AminoAcid.AA_ORDER.keys())

    @staticmethod
    def get_orders() -> Dict[str, str]:
        """Get all amino acid orderings"""

        return AminoAcid.AA_ORDER

    @staticmethod
    def get_order(order_name: str) -> str:
        """Get an amino acid ordering"""

        return AminoAcid.AA_ORDER[order_name]

    @staticmethod
    def get_order_names() -> ItemsView[str, str]:
        """Get all amino acid ordering names"""

        return AminoAcid.AA_ORDER_NAME.items()


    @staticmethod
    def list_properties() -> List[str]:
        """Get a list of all amino acid properties"""

        return list(AminoAcid.AA_PROPERTY.keys())

    @staticmethod
    def get_property(property_name: str, aa: str) -> float:
        """Get a specific property value for an amino acid"""

        if property_name not in AminoAcid.AA_PROPERTY:
            raise KeyError(f"Property '{property_name}' not found")
        elif aa not in AminoAcid.AA_PROPERTY[property_name]:
            raise KeyError(f"Amino acid '{aa}' not found in property '{property_name}'")

        return AminoAcid.AA_PROPERTY[property_name][aa]


    @staticmethod
    def list_color_schemes() -> List[str]:
        """Get a list of all available color scheme names"""

        return list(AminoAcid.AA_COLOR_SCHEME.keys())

    @staticmethod
    def get_color_scheme_names() -> ItemsView[str, str]:

        return AminoAcid.AA_COLOR_SCHEME_NAME.items()

    @staticmethod
    def get_color_scheme(scheme_name: str) -> Dict[str, str]:
        """Get a specific color scheme by name"""

        if scheme_name not in AminoAcid.AA_COLOR_SCHEME:
            raise KeyError(f"Color scheme '{scheme_name}' not found")
        return AminoAcid.AA_COLOR_SCHEME[scheme_name]

    @staticmethod
    def get_color(scheme_name: str, aa: str) -> str:
        """Get the color for a specific amino acid in a specific scheme"""

        scheme = AminoAcid.get_color_scheme(scheme_name)
        if aa not in scheme:
            raise KeyError(f"Amino acid '{aa}' not found in scheme '{scheme_name}'")
        return scheme[aa]
