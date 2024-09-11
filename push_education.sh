#!/bin/bash
set -e

TODAY=`date +%e_%m_%g`

git add .
git commit -m "$TODAY"
git push

echo "OK"


