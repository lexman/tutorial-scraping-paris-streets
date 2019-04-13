Scraping data with github action to publish a datapackage

# Intro
Open Knowledge Internationnal is aiming at easing the use of data with their frictionless data intitiative. They've specified datapackage [LINK] and developped tools for getting available open and publish it in an easyly usable format.

self descried
Easyly hosted 
ex : github for core packages :
* free
* track evolution of the data over time
* well known and vibrant community
* not locked-in : if github refuses to host pure data, of wants to charge, you can easealy change provider or go self hosting


Whether you use datapackage, the hard part when transforming data is keeping the result up to date. The purpose of this article is to show how you can acheive automatic update of data.



If you didn't want to host and setup your server to process data, you could already use online services to process data for a long time, like the very well-know Travis-CI, but it used to be quite complicated [LINK]. Now all the major code hosting plateforms like gitlab or butbicket provide integrated CI / CD features witch simplifies the process.
The most famous of all, github, has released a few weeks ago Github Actions 


Note : Ate the time of writing this, Github Action are still in beta, it means that :
* you have to sign up for the beta : https://github.com/features/actions
* action can only be enabled in private repository
* you can turn your repository public later : actions will still work but no one can see the actions


# Scrape on your laptop
## Functionnal description


## metadata

## setting up environnement 
python 3, virtualenv, gitignore ?

## get all streets from a page

## get all streets from the city

## save the csv

## test the data

# Automation with github actions

## install env

## run scrapper

## test the data

## commit


# Now

best way to start my own auto scrapping is forking the repo and changing the name of the dataset in :
* the metadata
* the scrapper
* the verifyer
* the commiter
* the licence
