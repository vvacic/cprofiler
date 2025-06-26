#!/usr/bin/env bash

cprof \
discover \
-Q ../data/alpha_morf.fa \
-D pdbs25 \
-I 10000 \
-A 0.05 \
-b

