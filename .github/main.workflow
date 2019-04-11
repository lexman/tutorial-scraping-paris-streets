workflow "Create datapackage" {
  on = "push"
  resolves = ["Publish"]
}

action "Install Scrapper" {
  uses = "./"
  args = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["Publish"]
}

action "Run scrapper" {
  uses = "./"
  needs = ["Install Scrapper"]
  args = "python scrapper.py"
}

action "Publish" {
  uses = "./"
  needs = ["Run scrapper"]
  runs = "./publish.sh"
  secrets = ["GITHUB_TOKEN"]
}
