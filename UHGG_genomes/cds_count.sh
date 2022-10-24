#!/bin/sh
FILE=$1.cds_count
if test -f "$FILE"; then
    rm $FILE
fi

while read lines; do
  #echo "$lines"
  IFS=',' read -r -a line <<< "$lines"
  protein_count=`less "../45_origin_faa_gff/${line[0]}.gff" | grep -v '^#' | awk '$3=="CDS"'  | wc -l`
  echo "$lines","$protein_count" >> $1.cds_count
done < $1
