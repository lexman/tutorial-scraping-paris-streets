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
    assert titles[0].text.startswith("Liste")
    assert titles[1].text.startswith("Voir aussi")
    all_li = titles[1].find_all_previous("li")
    labels = [clean_comment(li.text) for li in all_li]
    return labels


def streets_from(url, arrondissement):
    html = from_page(url)
    result = [(street, arrondissement, url) for street in find_all_streets(html)]
    return result
    

paris_1_url = (
    "https://fr.wikipedia.org/wiki/Liste_des_voies_du_1er_arrondissement_de_Paris"
)


def to_csv(table):
    res = "street,arrondissement_number,from_url\n"
    for (street, arrondissement, from_url) in table:
        res += "{},{},{}\n".format(street, arrondissement, from_url)
    return res
    
table = streets_from(paris_1_url, 1)
csv = to_csv(table)
with open("paris_streets.csv", "w") as f:
    f.write(csv)
