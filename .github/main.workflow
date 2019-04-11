workflow "Create datapackage" {
  resolves = ["Install Scrapper"]
  on = "push"
}

action "Install Scrapper" {
  uses = "docker://python:3.7-stretch"
  runs = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["Install Scrapper"]
}

action "docker://python:3.7-strech" {
  uses = "docker://python:3.7-strech"
  needs = ["Install Scrapper"]
  runs = "python scrapper.py"
}
