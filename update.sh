#!/bin/bash

gitegaPath=$1
email=$2

# Make sure the current working directory is the directory containing all the source files
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

output=$(date)
output="$output\n"

for account in $(find "$gitegaPath/" -maxdepth 1 ! -path . -type d -printf '%P\n' | sed 's/-github//g');
do
    output="$output\n\n$account\n"
    output="$output$(python update.py --name "$account")"
done

echo -e "Subject: Github stats update\r\n\r\n$output" | msmtp --from="$email" -t "$email"

