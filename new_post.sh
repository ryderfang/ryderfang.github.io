#! /bin/bash

hugo new posts/`date +%Y`/$1/index.md

echo "post '$1' created."
