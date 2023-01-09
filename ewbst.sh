#!/bin/bash


for model in `ls models | grep vec`;
do
    for query in `ls wntests/source-code/wbst/tests | grep $1.txt`;
        do
        # echo wntests/wbst+hwbst/$query models/$model
        python wntests/source-code/wbst/code/test_ewbst.py -m models/$model -t wntests/source-code/wbst/tests/$query >> ewbst_out.txt
        done
    done