workflow "Create datapackage" {
  on = "push"
  resolves = ["Run scrapper"]
}

action "Install Scrapper" {
  uses = "lexman/tutorial-scraping-paris-streets@master"
  args = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["Run scrapper"]
}

action "Run scrapper" {
  uses = "lexman/tutorial-scraping-paris-streets@master"
  needs = ["Install Scrapper"]
  args = "python scrapper.py"
}
