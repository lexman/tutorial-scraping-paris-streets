workflow "Create datapackage" {
  resolves = ["scrapper"]
  on = "push"
}

action "scrapper" {
  uses = "docker://python:3.7-stretch"
  runs = "python scrapper.py"
}

workflow "New workflow" {
  on = "schedule(0 0 * * *)"
  resolves = ["scrapper"]
}
