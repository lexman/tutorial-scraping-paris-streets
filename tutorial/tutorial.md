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
So what's the purpose here ? We want to make a datapackage with the streets of Paris. Our source is French Wikipedia. What is known as Paris is a gathering of 20 towns called ''arrondissement'', so we'll have to scrape each page mentioned in the [main article](https://fr.wikipedia.org/wiki/R%C3%A9seau_viaire_de_Paris) :

* https://fr.wikipedia.org/wiki/Liste_des_voies_du_1er_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_2e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_3e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_4e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_5e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_6e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_7e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_8e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_9e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_10e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_11e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_12e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_13e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_14e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_15e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_16e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_17e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_18e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_19e_arrondissement_de_Paris
* https://fr.wikipedia.org/wiki/Liste_des_voies_du_20e_arrondissement_de_Paris

We want to create a CSV file with 3 columns :
* name of the street
* number of the arrondissement because it is the administrative city of the street
* source : url of the page the informaton comes from

## metadata

Before we start scraping let's write the datapackage.json which describes this CSV :

''''
{
  "name": "paris-streets",
  "title": "All the streets of Paris, and their arrondissement",
  "version": "0.1.0",
  "license": "PDDL-1.0",
  "resources": [
    {
      "name": "paris-streets",
      "path": "data/paris-streets.csv",
      "format": "csv",
      "mediatype": "text/csv",
      "schema": {
        "fields": [
          {
            "name": "street",
            "description": "Name of the street",
            "type": "string"
          },
          {
            "name": "arrondissement",
            "description": "Number of the 'arrondissement' (administrative subdivision of Paris). There are numbered from 1 to 20. See https://en.wikipedia.org/wiki/Arrondissements_of_Paris",
            "type": "integer"
          },
          {
            "name": "from_url",
            "description": "Url of the web page that list this street",
            "type": "string"
          }
        ]
      }
    }
  ]
}

''''

Now we know what we what we want to build.



## setting up environnement 

We'll use the python [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) library to scrape the wikipedia pages. In Python, you shouldn't  install the library 
systemwide because you might break another program that uses another version of Beautiful Soup. 
 
The good practice is to intall it in a ''virtualenv'' which isolates your python environnement for your project. 
''''
virtualenv env
pip install bs4

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
