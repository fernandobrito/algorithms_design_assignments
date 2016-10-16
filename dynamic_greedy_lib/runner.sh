#!/bin/sh
# sh runner.sh
# sh runner.sh dynamic/tests/coin_change.py

if [ -z "$1" ]; then
    # If no arguments, run all files
    PATHS="dynamic/tests/* greedy/tests/*"

    for path in $PATHS
    do
        for file in $path
        do
          echo "[Running tests: $file]"
          PYTHONPATH=:`pwd`/utils/ python3.4 $file
          echo "\n"
        done
    done
else
    # If argument, run single file
    PYTHONPATH=:`pwd`/utils/ python3.4 $1
fi
