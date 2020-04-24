from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

site = urlopen("https://www.sports-reference.com/olympics/countries")
soup = BeautifulSoup(site, 'html.parser')
master_list = []
def scrape_table(site):
    rows = soup.find_all('tr', class_="")
    for row in rows:
        cells = row.find_all('td')
        country_list = []
        for td in cells:
            row = td.text
            row = row.strip(' \n\r\t')
            row = row.replace(u'\xa0', ' ')
            if row == '':
                row = 0
            country_list.append(row)
        master_list.append(country_list)
        print(master_list)

scrape_table(site)
def write_csv(site):
    csvfile = open('olympics.csv', 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow( ['number', 'country', 'first', 'last', 'participants', 'sports', 'gold', 'silver', 'bronze', 'total', 'first_winter', 'last_winter', 'participants_winter', 'sports_winter', 'gold_winter', 'silver_winter', 'bronze_winter', 'total_winter'] )
    for list in master_list:
        c.writerow(list)
    csvfile.close()
write_csv(site)
