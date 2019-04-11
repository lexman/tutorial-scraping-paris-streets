workflow "Create datapackage" {
  resolves = ["scrapper"]
  on = "push"
}

action "scrapper" {
  uses = "docker://python:3.7-stretch"
  runs = "pip install -r requirements.txt"
}

workflow "New workflow" {
  on = "schedule(0 0 * * *)"
  resolves = ["docker://python:3.7-strech"]
}

action "docker://python:3.7-strech" {
  uses = "docker://python:3.7-strech"
  needs = ["scrapper"]
  runs = "python scrapper.py"
}
