#!/bin/bash

YEAR="2025"
DAY=""

while getopts "y:d:" opt; do
    case $opt in
        y) YEAR="$OPTARG" ;;
        d) DAY="$OPTARG" ;;
        *) echo "Usage: $0 [-y year] [-d day]" >&2; exit 1;;
    esac
done

if [ -e "./src/y${YEAR}/day${DAY}" ]; then
    echo "Day $DAY of year $YEAR already exists!"
    exit 1
else
    mkdir -p "./src/y${YEAR}/day${DAY}"
    cp "./.template/template.py" "./src/y${YEAR}/day${DAY}/test_day${DAY}.py"
    touch "./src/y${YEAR}/day${DAY}/sample.txt"
    touch "./src/y${YEAR}/day${DAY}/full.txt"
    echo "Created directory and copied template for Year $YEAR Day $DAY."
fi
