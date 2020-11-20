#!/bin/sh -ex
target_branch="ghp-dev"
git config --global user.name "CircleCI deployer"
git config --global user.email "<>"
git checkout $target_branch
git reset --hard origin/main

echo "output of run.py: $(python run.py 1333)" > a.txt

git add run.py a.txt
git commit -m "[skip ci] updates GitHub Pages"
if [ $? -ne 0 ]; then
  echo "nothing to commit"
  exit 0
fi
git remote set-url origin "git@github.com:esperanto9657/myproj.git"
git push -f origin $target_branch
