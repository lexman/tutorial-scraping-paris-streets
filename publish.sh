#!/bin/bash

git config --global user.email "githubpublishbot@lexman.org"
git config --global user.name "Publish bot"
  
git add paris_streets.csv
git commit -m 'Changes in data'
git push
