"""
elections_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Jiří Nágl
email: nagl.jirka@seznam.cz
discord: jirkanagl
"""

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import sys

def script_do_excelu(url_vse, output):
    global soup_vse
    print(f"Stahuji data z vybraného URL: {url_vse}")
    odpoved_vse = requests.get(url_vse)
    soup_vse = BeautifulSoup(odpoved_vse.text, "html.parser")

def spoj_url():
    """Spojení url pro hledání v odkazu"""
    global soup_mesto, mesta_link
    odkaz_mest_1 = soup_vse.find_all(attrs={"headers":"t1sa1 t1sb1"})
    odkaz_mest_2 = soup_vse.find_all(attrs={"headers":"t2sa1 t2sb1"})
    odkaz_mest_3 = soup_vse.find_all(attrs={"headers":"t3sa1 t3sb1"})
    zakladni_url = "https://volby.cz/pls/ps2017nss/"
    mesta_link = []
    for td in odkaz_mest_1 + odkaz_mest_2 + odkaz_mest_3:
        link = td.find("a")
        if link is not None:
            href = link.get("href")
            uplna_url = urljoin(zakladni_url, href)
            mesta_link.append(uplna_url)


    odpoved_mesto = requests.get(mesta_link[0])
    soup_mesto = BeautifulSoup(odpoved_mesto.text, "html.parser")
def generování_hlavicky():
    """Vyscriptuje hlavičku z webu"""
    global nazvy_stran_list
    nazvy_stran = soup_mesto.find_all("td", class_= "overflow_name")
    nazvy_stran_list =[]
    for i in range(len(nazvy_stran)):
        strany = nazvy_stran[i].text.strip()
        nazvy_stran_list.append(strany)
    

def generovani_kodu_a_mesta():
    """"Vyscriptuje kód města a jeho název"""
    global kod_mesta_list, mesta_seznam_list
    kody = soup_vse.find_all("td", class_="cislo")
    mesta = soup_vse.find_all("td", class_="overflow_name")
    kod_mesta_list = []
    mesta_seznam_list = []
    for i in range(len(kody)):
        kod_mesta = kody[i].text.strip()
        mesta_seznam = mesta[i].text.strip()
        kod_mesta_list.append(kod_mesta)
        mesta_seznam_list.append(mesta_seznam)
        # writer.writerow([kod_mesta, mesta_seznam])

def generovani_celkových_poctu_a_hlasů(url):
    """"Vyscripuje celkové počty a počty hlasů jednotlivých politických stran"""
    global volici_text, obalky_text, platne_hlasy_text, strany_hlasy_list
    url_mesta = mesta_link[index]
    
    odpoved_mesta = requests.get(url_mesta)
    soup_mesta = BeautifulSoup(odpoved_mesta.text, "html.parser")
    volici_celkem = soup_mesta.find_all(attrs={"headers":"sa2"})
    obalky = soup_mesta.find_all(attrs={"headers":"sa3"})
    platne_hlasy = soup_mesta.find_all(attrs={"headers":"sa6"})
    strany_hlasy = soup_mesta.find_all(attrs={"headers":"t1sa2 t1sb3"})
    strany_hlasy_2 = soup_mesta.find_all(attrs={"headers":"t2sa2 t2sb3"})
    strany_hlasy_list = []
    for i in range(len(volici_celkem)):
        volici_text = volici_celkem[i].text.strip()
    for i in range(len(obalky)):
        obalky_text = obalky[i].text.strip()
    for i in range(len(platne_hlasy)):
        platne_hlasy_text = platne_hlasy[i].text.strip()
    for i in range(len(strany_hlasy)):
        strany_hlasy_text = strany_hlasy[i].text.strip()
        if strany_hlasy_text != "-":
            strany_hlasy_list.append(strany_hlasy_text)
    for i in range(len(strany_hlasy_2)):
        strany_hlasy_2_text = strany_hlasy_2[i].text.strip()
        if strany_hlasy_2_text != "-":
            strany_hlasy_list.append(strany_hlasy_2_text)



def export_do_excelu():
    global index
    print(f"Ukládám do souboru: {output}")
    with open (output, mode="w", newline="", encoding="utf-8") as file:
        spoj_url()
        generování_hlavicky()
        generovani_kodu_a_mesta()
        index = 0
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["code", "location", "registered", "envelopes", "valid"] + nazvy_stran_list)
        while index < len(kod_mesta_list):
            generovani_celkových_poctu_a_hlasů(mesta_link[index])
            writer.writerow([kod_mesta_list[index], mesta_seznam_list[index], volici_text, obalky_text, platne_hlasy_text] + strany_hlasy_list)
            index += 1
            continue
    print(f"Ukončuji program: {sys.argv[0]}")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Chyba argumentů. Zadejte 2 argumenty. URL a název výstupního souboru.")
        sys.exit(1)
    url_vse = sys.argv[1]
    output = sys.argv[2]
    if not (url_vse.startswith("http://") or url_vse.startswith("https://")):
        print("Chyba. První argument musí být URL adresa.")
        sys.exit(1)
    if not output.endswith(".csv"):
        print("Chyba. Druhý argument musíí být CSV soubor")
        sys.exit(1)
    script_do_excelu(url_vse, output)
    export_do_excelu()



