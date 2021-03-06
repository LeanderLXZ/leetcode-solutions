#!/bin/bash
# Move files to problems from working folder

for file_path in $(ls working/*)
do
  file=${file_path#"working/"}
  file=${file[@]%\.*}
  echo "Moving $file_path to problems/$file/"
  mkdir problems/$file
  mv $file_path problems/$file
done