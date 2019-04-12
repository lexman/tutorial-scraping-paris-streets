workflow "Create datapackage" {
  on = "push"
  resolves = ["Publish"]
}

action "Install Scrapper" {
  uses = "docker://python:3.7-stretch"
  runs = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["Publish"]
}

action "Run scrapper" {
  uses = "docker://python:3.7-stretch"
  needs = ["Install Scrapper"]
  runs = "python scrapper.py"
}

action "Publish" {
  uses = "docker://python:3.7-stretch"
  needs = ["Run scrapper"]
  runs = "./publish.sh"
  secrets = ["GITHUB_TOKEN"]
}
