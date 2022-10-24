#!/bin/sh
while read download_list
do
        wget ${download_list}
done <$1
