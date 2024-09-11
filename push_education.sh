#!/bin/bash
set -e

TODAY=`date +%G-%m-%d`

git add .
git commit -m "$TODAY"
git push

echo "OK"


