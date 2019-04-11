workflow "Create datapackage" {
  on = "push"
  resolves = [""]
}

action "Install Scrapper" {
  uses = "docker://python:3.7-stretch"
  args = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["Run scrapper"]
}

action "Run scrapper" {
  uses = "docker://python:3.7-stretch"
  needs = ["Install Scrapper"]
  args = "python scrapper.py"
}
