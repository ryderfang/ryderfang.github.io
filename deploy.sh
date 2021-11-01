#! /bin/bash

# waiting for build complete
result=`hugo --buildDrafts`
git add .
git commit -m "Deploy(auto commit)"
git push origin master

