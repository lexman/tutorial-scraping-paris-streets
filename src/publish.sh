#!/bin/bash

set -eux

git config --global user.email "githubpublishbot@lexman.org"
git config --global user.name "Publish bot"
  
git add data/paris_streets.csv && git commit -m 'Data has changed' && git push origin $GITHUB_REF ; echo " "
