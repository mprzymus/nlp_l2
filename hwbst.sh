#!/bin/bash


for model in `ls models | grep vec`;
do
    for query in `ls wntests/wbst+hwbst | grep $1.hwbst.csv`;
        do
        # echo wntests/wbst+hwbst/$query models/$model
        python wntests/source-code/wbst/code/test_ewbst.py -m models/$model -t wntests/wbst+hwbst/$query >> hwbst_out.txt
        done
    done