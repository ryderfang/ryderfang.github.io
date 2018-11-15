#! /bin/bash

# waiting for build complete
result = `jekyll build`
git add .
git commit -m "Update(auto commit)"
git push origin master

