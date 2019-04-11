workflow "Create datapackage" {
  on = "push"
  resolves = ["GitHub Action for Python"]
}

action "Install Scrapper" {
  uses = "./"
  args = "pip install -r requirements.txt"
}

workflow "Run every day" {
  on = "schedule(0 0 * * *)"
  resolves = ["GitHub Action for Python-2"]
}

action "Run scrapper" {
  uses = "./"
  needs = ["Install Scrapper"]
  args = "python scrapper.py"
}

action "./" {
  uses = "./"
  needs = ["Run scrapper"]
  secrets = ["GITHUB_TOKEN"]
  runs = "ls -lisah "
}

action "GitHub Action for Python" {
  uses = "./"
  needs = ["./"]
  runs = "git status"
}

action "GitHub Action for Python-1" {
  uses = "./"
  needs = ["Run scrapper"]
  runs = "git add paris_streets.csv"
}

action "GitHub Action for Python-2" {
  uses = "./"
  needs = ["GitHub Action for Python-1"]
  runs = "git commit -m \"Changes in data\""
  secrets = ["GITHUB_TOKEN"]
}
