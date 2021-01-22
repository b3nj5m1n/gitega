#!/bin/bash

gitegaPath=$1
account=$2
repository=$3
accountPath=$4

# Make sure the current working directory is the directory containing all the source files
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

python exportCsv.py "$account" "$repository" --rootDir "$gitegaPath" --output "$accountPath/statsData/$repository/data.csv" --no-pipe

cd "$accountPath/statsData/$repository/" 
cat "$DIR/plotTemplate.gnuplot" | gnuplot
