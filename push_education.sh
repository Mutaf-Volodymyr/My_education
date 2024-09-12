#!/bin/bash
set -e

TODAY=`date +%G-%m-%d`

git add .
git commit -m "$TODAY_${BASH_ARGV[0]}"
git push

echo "OK"


