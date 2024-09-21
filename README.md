# Engeto_3_projekt
Třetí projekt na Python Akademii od Engeta.
# Popis projektu
Tento projekt slouží k extrahování výsledků palamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).
# Instalace knihoven
Knihovny, které jsou použity v kódujsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip3 --version # overim verzi manazeru
$ pip3 install -r requirements.txt # nainstalujeme knihovny
```
# Spuštění projektu
Spuštění souboru elections_scrapers.py v rámci příkazového řádku požaduje dva povinné argumenty.
```
python elections_scrapers.py <odkaz-uzemniho-celku> <vysledny-soubor>
```
Následně se vám stáhnou výsledky jako soubor s příponou .csv.
# Ukázka projektu
Výsledky hlasování pro okres Prostějov:
```
1. argument https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument vysledky_prostejov.csv
```
Spuštění programu:
```
python elections_scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_prostejov.csv'
```
Průběh stahování:
```
Stahuji data z vybraného URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
Ukládam do souboru: vysledky_prostejov.csv
Ukončuji elections_scraper
```
Částečný výstup:
```
code, location, registered, envelopes, valid, ...
506761, Alojzov, 205, 145, 144, 29, 0, 0, 9, 0, 5, 17, 4, 1, ...
589268, Bedihošť, 834, 527, 524, 51, 0, 0, 28, 1, 13, 123, 2, 2, ...
```



