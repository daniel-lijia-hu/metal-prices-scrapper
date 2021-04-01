# Library imports

import requests
from bs4 import BeautifulSoup
import csv

# Links where the data comes from

urls = ["https://finance.yahoo.com/quote/ALI%3DF/history?p=ALI%3DF",
       "https://finance.yahoo.com/quote/HG%3DF/history?p=HG%3DF",
       "https://finance.yahoo.com/quote/GC%3DF/history?p=GC%3DF",
       "https://finance.yahoo.com/quote/SI%3DF/history?p=SI%3DF"]
       
# The following script will obtain the data from the latest 30 days
values_to_csv = {}       
for url in range(0, len(urls)):
    page = requests.get(urls[url]).content
    soup = BeautifulSoup (page, 'lxml')
    all_data = soup.find_all('tbody')
    rows = all_data[0].find_all('tr')
    for i in range(0, len(rows)):
        values = rows[i].find_all('td')
        day = dt.datetime.strptime(values[0].text, '%b %d, %Y')
        day = day.strftime('%d/%m/%Y')
        if day not in values_to_csv.keys():
            values_to_csv[day] = [None, None, None, None]
        if values[1].text == '-':
            values_to_csv[day][url] = None
        else:
            cost = values[1].text.replace(',',"").replace('.',",")
            values_to_csv[day][url] = cost
            
# The following script writes a .csv with the latest prices
csv_columns = ['Day', 'Al Price', 'Cu Price', 'Au Price', 'Ag Price']
csv_file = 'metals_latest_data.csv'
with open (csv_file, 'w') as output:
    csv_output = csv.writer(output, delimiter=';')
    csv_output.writerow(csv_columns)
    for key in values_to_csv.keys():
        csv_output.writerow([key] + values_to_csv[key])
