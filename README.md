> Live web app is at [http://www.cprofiler.org](http://www.cprofiler.org)

Composition Profiler - version 2.0 (June 2025)

Copyright (c) 2025 Vladimir Vacic, Vladimir N. Uversky, A. Keith Dunker,
Stefano Lonardi.

Composition Profiler is a tool for semi-automatic discovery of
enrichment or depletion of amino acids, either individually or grouped
by their physico-chemical or structural properties, such as
aromaticity, charge, polarity, hydrophobicity, flexibility, surface
exposure, solvation potential, interface propensity, normalized
frequency of occurrence in α helices, β structures, and coils, linker
and disorder propensities, size and bulkiness.

The program takes two samples of amino acids as input: a query sample
and a reference sample. The latter provides a suitable background amino
acid distribution, and should be chosen according to the nature of the
query sample, for example, a standard protein database (e.g. SwissProt,
PDB Select 25, DisProt, or surface residues of monomeric proteins), a
representative sample of proteins from the organism under study, or a
group of proteins with a contrasting functional annotation. The results
of the analysis of amino acid composition differences are summarized in
textual and graphical form.

The graphical output is a bar chart composed of twenty data points
(one for each amino acid), where bar heights indicate enrichment or
depletion. The output is designed to assist the discovery of
statistically significant composition anomalies by color-coding and
sorting residues according to their physico-chemical properties. For
example, if the property being tested is flexibility, the tool will
group rigid amino acids on the left hand side of the plot and flexible
amino acids on the right hand side of the plot.

As an exploratory data mining tool, our software can be used to guide
feature selection for protein function or structure predictors. For
classes of proteins with significant differences in frequencies of
amino acids having particular physico-chemical (e.g. hydrophobicity or
charge) or structural (e.g. α helix propensity) properties,
Composition Profiler can be used as a rough, light-weight visual
classifier.

In citing Composition Profiler, please refer to:

> Vacic V, Uversky VN, Dunker AK, Lonardi S. (2007)
"Composition Profiler: A tool for discovery and visualization of amino
 acid composition differences." *BMC Bioinformatics*. 8:211.
 [PMID:17578581](https://pubmed.ncbi.nlm.nih.gov/17578581/).

Composition Profiler was rewritten from scratch in python, using numpy
for sampling and statistical computation, and flask for the web front
end. This greatly simplified the codebase and made installation a
breeze.  

(The original version was written in ruby with some routines written in
C and using numerical approximation functions from the Stephen L.
Moshier's [Cephes Math Library](http://www.netlib.org/cephes)).

Also, computers became much faster since 2007, making bootstrap and
permutation sampling an efficient way to approximate non-anaytical
distributions (and more accurate to boot).  

What a difference 18 years make.


## Contents:

* cprofiler   - python package cprofiler 
* cprof_flask - Front end web interface 


## System requirements:

nginx and gunicorn for serving the flask application and static html
pages (help, examples, etc.). See [SETUP_SERVER.md](SETUP_SERVER.md) 
for details.

python (with numpy, pandas, matplotlib, flask packages installed). See
[SETUP_PYTHON.md](SETUP_PYTHON.md) for details.



## Command line interface:

```
$ cprof -h
usage: cprof [-h] {discover,plot,relent} ...

positional arguments:
  {discover,plot,relent}
    discover            Discover significant fractional differences
    plot                Plot fractional differences
    relent              Compute relative entropy

options:
  -h, --help            show this help message and exit
```


### Module discover:

```
$ cprof discover -h
usage: cprof discover [-h] -Q QUERY_FILE [-B BACKGROUND_FILE | -D {sprot,pdbs25,surface,disprot}]
                      [-I ITERATIONS] [-A ALPHA] [-b]

options:
  -h, --help            show this help message and exit
  -Q QUERY_FILE         Query file in FastA format
  -B BACKGROUND_FILE    Background file in FastA format
  -D {sprot,pdbs25,surface,disprot}
                        Preset background distribution. One of the following:
                        
                        sprot        Proteins from SwissProt 51
                        pdbs25       PDB Select 25
                        surface      Surface residues of monomers from PDB
                        disprot      Disordered regions from DisProt 3.4
                        
                        Defaults to sprot.
  -I ITERATIONS         Number of bootstrap iterations. Defaults to 10,000.
  -A ALPHA              Significance value for statistical tests. Defaults to 0.05.
  -b                    Apply Bonferroni correction. Off by default.
```


### Module plot

```
$ cprof plot -h
usage: cprof plot [-h] -Q QUERY_FILE -O OUTPUT_FILE [-B BACKGROUND_FILE | -D {sprot,pdbs25,surface,disprot}]
                  [-I ITERATIONS]
                  [-X {diff,alpha,hydrophobicity_eisenberg,hydrophobicity_kyte,hydrophobicity_fauchere,surface_janin,flexibility_vihinen,interface_propensity_jones,solvation_jones,bulikness_zimmerman,polarity_zimmerman,linker_george,alpha_nagano,beta_nagano,coil_nagano,size_dawson}]
                  [-Y YLAB]
                  [-C {mono,weblogo,amino,shapley,aromatic,charged,hydrophobicity_eisenberg,hydrophobicity_kyte,hydrophobicity_fauchere,surface_janin,flexibility_vihinen,interface_propensity_jones,solvation_jones,disorder_dunker,bulkiness_zimmerman,polarity_zimmerman,linker_george,alpha_nagano,beta_nagano,coil_nagano,size_dawson}]
                  [-F {png,pdf,eps,txt}] [-W IMAGE_WIDTH] [-H IMAGE_HEIGHT] [-U {inch,cm,pixel}]
                  [-R RESOLUTION]

options:
  -h, --help            show this help message and exit
  -Q QUERY_FILE         Query file in FastA format
  -O OUTPUT_FILE        Output file
  -B BACKGROUND_FILE    Background file in FastA format
  -D {sprot,pdbs25,surface,disprot}
                        Preset background distribution. One of the following:
                        
                        sprot        Proteins from SwissProt 51
                        pdbs25       PDB Select 25
                        surface      Surface residues of monomers from PDB
                        disprot      Disordered regions from DisProt 3.4
                        
                        Defaults to sprot.
  -I ITERATIONS         Number of bootstrap iterations. Defaults to 10,000.
  -X {diff,alpha,hydrophobicity_eisenberg,hydrophobicity_kyte,hydrophobicity_fauchere,surface_janin,flexibility_vihinen,interface_propensity_jones,solvation_jones,bulikness_zimmerman,polarity_zimmerman,linker_george,alpha_nagano,beta_nagano,coil_nagano,size_dawson}
                        Amino acid ordering. Sorts residues in the increasing order of one of the
                        physicochemical or structural properties:
                        
                        diff                       By observed differences
                        alpha                      Alphabetical
                        hydrophobicity_eisenberg   Hydrophobicity (Eisenberg)
                        hydrophobicity_kyte        Hydrophobicity (Kyte-Doolittle)
                        hydrophobicity_fauchere    Hydrophobicity (Fauchere-Pliska)
                        surface_janin              Surface exposure (Janin)
                        flexibility_vihinen        Flexibility (Vihinen)
                        interface_propensity_jones Interface propensity (Jones-Thornton)
                        solvation_jones            Solvation potential (Jones-Thornton)
                        bulikness_zimmerman        Bulkiness (Zimmerman)
                        polarity_zimmerman         Polarity (Zimmerman)
                        linker_george              Linker propensity (George-Heringa)
                        alpha_nagano               Alpha helix propensity (Nagano)
                        beta_nagano                Beta structure propensity (Nagano)
                        coil_nagano                Coil propensity (Nagano)
                        size_dawson                Size (Dawson)
                        
                        Defaults to ordering By observed differences.
  -Y YLAB               Y-axis label
  -C {mono,weblogo,amino,shapley,aromatic,charged,hydrophobicity_eisenberg,hydrophobicity_kyte,hydrophobicity_fauchere,surface_janin,flexibility_vihinen,interface_propensity_jones,solvation_jones,disorder_dunker,bulkiness_zimmerman,polarity_zimmerman,linker_george,alpha_nagano,beta_nagano,coil_nagano,size_dawson}
                        Color scheme. One of the following:
                        
                        mono                       Monochromatic
                        weblogo                    Weblogo color scheme
                        amino                      Amino color scheme
                        shapley                    Shapley color scheme
                        aromatic                   Aromatic residues
                        charged                    Charged residues
                        hydrophobicity_eisenberg   Hydrophobicity (Eisenberg)
                        hydrophobicity_kyte        Hydrophobicity (Kyte-Doolittle)
                        hydrophobicity_fauchere    Hydrophobicity (Fauchere-Pliska)
                        surface_janin              Surface exposure (Janin)
                        flexibility_vihinen        Flexibility (Vihinen)
                        interface_propensity_jones Interface propensity (Jones-Thornton)
                        solvation_jones            Solvation potential (Jones-Thornton)
                        disorder_dunker            Disorder propensity (Dunker)
                        bulkiness_zimmerman        Bulkiness (Zimmerman)
                        polarity_zimmerman         Polarity (Zimmerman)
                        linker_george              Linker propensity (George-Heringa)
                        alpha_nagano               Alpha helix propensity (Nagano)
                        beta_nagano                Beta structure propensity (Nagano)
                        coil_nagano                Coil propensity (Nagano)
                        size_dawson                Size (Dawson)
                        
                        Defaults to Monochromatic.
  -F {png,pdf,eps,txt}  Output format. Defaults to png.
  -W IMAGE_WIDTH        Width of output image. Defaults to 5.
  -H IMAGE_HEIGHT       Height of output image. Defaults to 3.5.
  -U {inch,cm,pixel}    Image size units. Defaults to inch.
  -R RESOLUTION         Bitmap resolution in dpi. Defaults to 300.
```


### Module for relative entropy calculations

```
$ cprof relent -h
usage: cprof relent [-h] -Q QUERY_FILE [-B BACKGROUND_FILE | -D {sprot,pdbs25,surface,disprot}] [-I ITERATIONS]

options:
  -h, --help            show this help message and exit
  -Q QUERY_FILE         Query file in FastA format
  -B BACKGROUND_FILE    Background file in FastA format
  -D {sprot,pdbs25,surface,disprot}
                        Preset background distribution. One of the following:
                        
                        sprot        Proteins from SwissProt 51
                        pdbs25       PDB Select 25
                        surface      Surface residues of monomers from PDB
                        disprot      Disordered regions from DisProt 3.4
                        
                        Defaults to sprot.
  -I ITERATIONS         Number of bootstrap iterations. Defaults to 10,000.
```


## Comand line usage examples:

Simple command line examples for discovery and plotting of composition 
differences in α MoRF residues:

```
cprof \
discover \
-Q data/alpha_morf.fa \
-D pdbs25 \
-I 10000 \
-A 0.05 \
-b
```

```
cprof \
plot \
-Q data/alpha_morf.fa \
-D pdbs25 \
-X flexibility_vihinen \
-Y "(Alpha MoRF - PDBS25) / PDBS25" \
-C disorder_dunker \
-O alpha.pdf \
-F pdf
```


```
cprof \
relent \
-Q data/alpha_morf.fa \
-D pdbs25 \
-I 10000
```
