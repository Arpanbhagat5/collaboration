#!/bin/bash
suffix="mod"
# location=$(pwd)/*.txt
user_location=$1/*.txt
if [[ ! -z $1 ]]; then
echo "ran if"
echo "All the files Before rename"
echo $(ls)
echo "Selected files for rename"
for f in ${user_location}
do
    echo ${f}
    extn=$(echo ${f} | cut -d "." -f 2)
    name=$(echo ${f} | cut -d "." -f 1)
    if [[ $(echo $name | tail -c 5 ) != "-mod" ]]; then
    mv $f ${name}-${suffix}.${extn}
    fi
done
echo "All the files After rename"
ls -1 $1
else
echo "didnt run if"
fi