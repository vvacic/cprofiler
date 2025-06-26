#!/usr/bin/env bash

cprof \
plot \
-Q ../data/alpha_morf.fa \
-D pdbs25 \
-X flexibility_vihinen \
-Y "(Alpha MoRF - PDBS25) / PDBS25" \
-C disorder_dunker \
-O alpha.pdf \
-F pdf

