#! /bin/bash

cd themes/uBlogger

git remote add upstream git@github.com:uPagge/uBlogger.git

git fetch upstream

git checkout master

git rebase upstream/master
