#!/bin/bash

# Make sure the current working directory is the directory containing all the source files
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

for account in $(find ~/.gitega/ -maxdepth 1 ! -path . -type d -printf '%P\n' | sed 's/-github//g');
do
    python update.py --name "$account"
done
