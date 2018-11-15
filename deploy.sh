#! /bin/bash

jekyll build
git add .
git commit -m "Update(auto commit)"
git push origin master

