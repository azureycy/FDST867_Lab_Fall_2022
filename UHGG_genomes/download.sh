#!/bin/sh
while read download_list
do
        wget -P ../44_origin_faa_gff/ ${download_list}
done <$1
