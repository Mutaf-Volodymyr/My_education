#!/bin/bash
set -e

path_to_dir="/opt/290724-ptm/Mutaf/HW_19"

# created two directory
mkdir -p $path_to_dir/dir1 $path_to_dir/dir2

# cteated 100 files whith random name
for i in {1..100}
  do
  touch  $path_to_dir/dir1/$RANDOM
  done

# move file if name is even
for file in $path_to_dir/dir1/*;
  do
  filename=$(basename "$file")
  if (( filename % 2 == 0 ));
     then
     mv "$file" $path_to_dir/dir2/
  fi
  done