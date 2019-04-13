workflow "Create datapackage" {
  on = "push"
  resolves = ["Publish"]
}

action "Install Scrapper" {
  uses = "./action-virtualenv"
  args = "pip install -r src/requirements.txt"
}

workflow "Run every day" {
  resolves = ["Publish"]
  on = "schedule(0 * * * *)"
}

action "Run scrapper" {
  uses = "./action-virtualenv"
  needs = ["Install Scrapper"]
  args = "python src/scrapper.py"
}

action "Publish" {
  uses = "./action-virtualenv"
  needs = ["Run scrapper"]
  runs = "src/publish.sh"
  secrets = ["GITHUB_TOKEN"]
}
