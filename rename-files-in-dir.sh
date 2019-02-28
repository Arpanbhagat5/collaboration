#!/bin/bash
suffix="mod"
location=$(pwd)/*.txt
echo "All the files Before rename"
echo $(ls)
echo "Selected files for rename"
for f in $location
do
    echo $f
    mv $f $f$suffix
done
echo "All the files After rename"
echo $(ls)
