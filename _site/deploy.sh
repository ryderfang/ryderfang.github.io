#! /bin/bash

# waiting for build complete
result=`bundle exec jekyll build`
git add .
git commit -m "Update(auto commit)"
git push origin master

