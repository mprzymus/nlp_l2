#!/bin/bash

python3 scripts/facebook_bin_2_vec.py models/cbow_full.bin > models/cbow_full.vec
python3 scripts/facebook_bin_2_vec.py models/cbow_corpus.bin > models/cbow_corpus.vec

python3 scripts/facebook_bin_2_vec.py models/sg_full.bin > models/sg_full.vec
python3 scripts/facebook_bin_2_vec.py models/sg_corpus.bin > models/sg_corpus.vec
