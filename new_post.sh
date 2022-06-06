#! /bin/bash

if [ $# != 2 ]; then
    echo "缺少参数: eg. ./new_post.sh [pst/lc] [post-name]"
    exit 1
fi

if [ $1 = "pst" ]; then
    hugo new posts/`date +%Y`/$2/index.md
else
    hugo new leetcode/$2/index.md
fi

echo "post '$2' created."
