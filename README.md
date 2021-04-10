# Pràctica 1: Web scraping

## Descripció
Aquesta pràctica s'ha realitzat en l'assignatura de Tipologia i cicle de vida de les dades de la Universitat Oberta de Catalunya

## Membres de l'equip
L'activitat ha estat elaborada per l'equip format per Jordi Gual Obradors i Daniel Lijia Hu

## Fitxers del codi font

### Fitxers py
* MetalHistoricData.py: serveix per representar gràficament les dades històriques del metall dels últims anys. La granularitat d'aquestes dades és mensual.
* MetalPriceScrapper.py: serveix per obtenir les dades dels últims preus mitjançant scrapping dels metalls en qüestió (Alumini, coure, or i plata), i crear-ne un .csv amb aquests.
* La seva granularitat és diària.

### Fitxers csv
* metals.csv: arxiu que llegeix l'script MetalHistoricData.py per representar gràficament les dades històriques
* metals_latest_data.csv: output obtingut de MetalPriceScrapper.py (també es pot veure, executat a dia 6 d'abril de 2021, al següent link) http://doi.org/10.5281/zenodo.4667668

### Fitxers PDF
* report.pdf: arxiu que respon les preguntes plantejades de la pràctica 1
