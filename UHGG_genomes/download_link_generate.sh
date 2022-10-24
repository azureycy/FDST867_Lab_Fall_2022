#!/bin/sh
while read lines; do
  echo "https://www.ebi.ac.uk/metagenomics/api/v1/genomes/${lines}/downloads/${lines}.gff" >> download_gff.txt
  echo "https://www.ebi.ac.uk/metagenomics/api/v1/genomes/${lines}/downloads/${lines}.faa" >> download_faa.txt
done < $1
