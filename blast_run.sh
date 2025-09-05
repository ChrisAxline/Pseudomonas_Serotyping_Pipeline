#!/bin/bash

query_dir=/Users/chrisaxline/Desktop/ALIKI_Isolates/PASP
out_dir=~/Desktop/PASP_serotype_blast_results
db=/Users/chrisaxline/Desktop/PAst-master/OSAdb   # path to your DB prefix (without .nsq etc.)

mkdir -p "$out_dir"

for query in "$query_dir"/*.fasta "$query_dir"/*.fna; do
    [ -e "$query" ] || continue  # skip if no files found
    base=$(basename "$query")
    base=${base%.*}  # strip extension
    blastn -query "$query" -db "$db" -out "$out_dir/${base}_vs_db.txt" -outfmt 6
done
