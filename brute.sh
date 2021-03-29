#!/bin/bash
valid=true
count=1
while [ $valid ]
do
echo "Count value" $count
7z x locked.zip -y -papa112
if [ $count -eq 5 ];
then
break
fi
((count++))
done
