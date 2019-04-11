workflow "Create datapackage" {
  on = "push"
  resolves = ["Run scrapper"]
}

action "Install Scrapper" {
  uses = "docker://python:3.7-stretch"
  args = "pip install -r requirements.txt"
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

action "Run scrapper" {
  uses = "docker://python:3.7-stretch"
  needs = ["Install Scrapper"]
  args = "python scrapper.py"
}
