#! /bin/bash

cd themes/congo

#git remote add origin git@github.com:ryderfang/congo.git
#git remote add upstream git@github.com:jpanther/congo.git

git fetch upstream

git checkout stable

git rebase upstream/stable

git push origin stable
