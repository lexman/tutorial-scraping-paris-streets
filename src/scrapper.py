from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from os.path import exists


def from_page(url):
    filename = url.split("/")[-1]
    if not exists(filename):
        urlretrieve(url, filename) 
    return open(filename).read()


def clean_comment(name_with_parenthesis):
    return name_with_parenthesis.split("(")[0].strip()


def find_all_streets(html):
    soup = BeautifulSoup(html)
    titles = soup.find_all("h2")
    assert titles[0].text.startswith("Liste"), titles[0].text
    assert titles[1].text.startswith("Voir aussi"), titles[1].text
    all_li = titles[1].find_all_previous("li")
    labels = [clean_comment(li.text) for li in all_li]
    return labels


def streets_from(url, arrondissement):
    html = from_page(url)
    result = [(street, arrondissement, url) for street in find_all_streets(html)]
    return result


urls = [
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_1er_arrondissement_de_Paris", 1),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_2e_arrondissement_de_Paris", 2),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_3e_arrondissement_de_Paris", 3),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_4e_arrondissement_de_Paris", 4),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_5e_arrondissement_de_Paris", 5),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_6e_arrondissement_de_Paris", 6),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_7e_arrondissement_de_Paris", 7),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_8e_arrondissement_de_Paris", 8),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_9e_arrondissement_de_Paris", 9),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_10e_arrondissement_de_Paris", 10),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_11e_arrondissement_de_Paris", 11),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_12e_arrondissement_de_Paris", 12),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_bois_de_Vincennes", 12),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_13e_arrondissement_de_Paris", 13),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_14e_arrondissement_de_Paris", 14),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_15e_arrondissement_de_Paris", 15),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_16e_arrondissement_de_Paris", 16),
#    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_bois_de_Boulogne", 16),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_17e_arrondissement_de_Paris", 17),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_18e_arrondissement_de_Paris", 18),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_19e_arrondissement_de_Paris", 19),
    ("https://fr.wikipedia.org/wiki/Liste_des_voies_du_20e_arrondissement_de_Paris", 20),
]

def to_csv(table):
    res = "street,arrondissement_number,from_url\n"
    for (street, arrondissement, from_url) in table:
        res += "{},{},{}\n".format(street, arrondissement, from_url)
    return res

table = []
for (url, num_arrondissement) in urls:    
    print("Scraping {}\n".format(url))
    table += streets_from(url, num_arrondissement)
csv = to_csv(table)
with open("paris_streets.csv", "w") as f:
    f.write(csv)
