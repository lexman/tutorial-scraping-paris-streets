from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
from os.path import exists, join
from os import mkdir
from itertools import groupby
from operator import itemgetter


def read_page(url):
    return urlopen(url).read()


def clean_comment(name_with_parenthesis):
    return name_with_parenthesis.split("(")[0].strip()


def find_all_streets(html):
    soup = BeautifulSoup(html)
    titles = soup.find_all("h2")
    assert titles[0].text.startswith("Liste"), titles[0].text
    assert titles[1].text.startswith("Voir aussi") or \
           titles[1].text.startswith("Source") or \
           titles[1].text.startswith("Par type"), titles[1].text
    all_li = titles[1].find_all_previous("li")
    labels = [clean_comment(li.text) for li in all_li if clean_comment(li.text) != ""]
    return labels


# From https://docs.python.org/3/library/itertools.html#itertools-recipes
def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return map(next, map(itemgetter(1), groupby(iterable, key)))
    

def save_csv(records):
    SAVE_DIR = 'data'
    SAVE_FILE = join(SAVE_DIR, 'paris-streets.csv')
    if not exists(SAVE_DIR):
        mkdir(SAVE_DIR);
    HEADER = ['street','arrondissement','from_url']
    writer = csv.writer(open(SAVE_FILE, 'w'), lineterminator='\n')
    writer.writerow(HEADER)
    writer.writerows(records)    


URLS = [
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_1er_arrondissement_de_Paris", 1),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_2e_arrondissement_de_Paris", 2),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_3e_arrondissement_de_Paris", 3),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_4e_arrondissement_de_Paris", 4),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_5e_arrondissement_de_Paris", 5),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_6e_arrondissement_de_Paris", 6),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_7e_arrondissement_de_Paris", 7),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_8e_arrondissement_de_Paris", 8),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_9e_arrondissement_de_Paris", 9),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_10e_arrondissement_de_Paris", 10),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_11e_arrondissement_de_Paris", 11),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_12e_arrondissement_de_Paris", 12),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_bois_de_Vincennes", 12),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_13e_arrondissement_de_Paris", 13),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_14e_arrondissement_de_Paris", 14),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_15e_arrondissement_de_Paris", 15),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_16e_arrondissement_de_Paris", 16),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_bois_de_Boulogne", 16),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_17e_arrondissement_de_Paris", 17),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_18e_arrondissement_de_Paris", 18),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_19e_arrondissement_de_Paris", 19),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_20e_arrondissement_de_Paris", 20),
]
    

records = []
for (url, num_arrondissement) in URLS:    
    print("Scraping {}\n".format(url))
    html = read_page(url)
    arrondissement_records = [(street, num_arrondissement, url) for street in find_all_streets(html)]
    # Sorting ensure easy tracking of modifications in git
    arrondissement_records.sort(key=lambda s: s[0].lower())
    records += unique_justseen(arrondissement_records)

save_csv(records)
