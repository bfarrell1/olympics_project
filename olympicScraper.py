from bs4 import BeautifulSoup
import requests
import csv

start = 'https://www.sports-reference.com/olympics/countries/'
page = requests.get(start)
soup = BeautifulSoup(page.text, 'html.parser')
countries = ['AFG', 'ALB', 'ALG', 'ASA', 'AND', 'ANG','ANT', 'ARG', 'ARM', 'ARU', 'ANZ', 'AUS', 'AUT', 'AZE', 'BAH', 'BRN', 'BAN', 'BAR', 'BLR', 'BEL', 'BIZ', 'BEN', 'BER', 'BHU', 'BOH', 'BOL', 'BIH', 'BOT', 'BRA', 'IVB', 'BRU', 'BUL', 'BUR', 'BDI', 'CAM', 'CMR', 'CAN', 'CPV', 'CAY', 'CAF', 'CHA', 'CHI', 'CHN', 'TPE', 'COL', 'COM', 'CGO', 'COD', 'COK', 'CRC', 'CIV', 'CRO', 'CUB', 'CYP', 'CZE', 'TCH', 'DEN', 'DJI', 'DMA', 'DOM', 'GDR', 'ECU', 'EGY', 'ESA', 'GEQ', 'ERI', 'EST', 'ETH', 'FSM', 'FIJ', 'FIN', 'FRA', 'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GBR', 'GRE', 'GRN', 'GUM', 'GUA', 'GUI', 'GBS', 'GUY', 'HAI', 'HON', 'HKG', 'HUN', 'ISL', 'IND', 'IOA', 'INA', 'IRI', 'IRQ', 'IRL', 'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOS', 'KUW', 'KGZ', 'LAO', 'LAT', 'LIB', 'LES', 'LBR', 'LBA', 'LIE', 'LTU', 'LUX', 'MKD', 'MAD', 'MAW', 'MAL', 'MAS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTN', 'MRI', 'MEX', 'MDA', 'MON', 'MGL', 'MNE', 'MAR', 'MOZ', 'MYA', 'NAM', 'NRU', 'NEP', 'NED', 'AHO', 'NZL', 'NFL', 'NCA', 'NGR', 'NIG', 'NBO', 'PRK', 'YAR', 'NOR', 'OMA', 'PAK', 'PLW', 'PLE', 'PAN', 'PNG', 'PAR', 'PER', 'PHI', 'POL', 'POR', 'PUR', 'QAT', 'ROT', 'RHO', 'ROU', 'RUS', 'RWA', 'SAA', 'SKN', 'LCA', 'VIN', 'SAM', 'SMR', 'STP', 'KSA', 'SEN', 'SRB', 'SCG', 'SEY', 'SLE', 'SGP', 'SVK', 'SLO', 'SOL', 'SOM', 'RSA', 'KOR', 'SSD', 'VNM', 'YMD', 'URS', 'ESP', 'SRI', 'SUD', 'SUR', 'SWZ', 'SWE', 'SUI', 'SYR', 'TJK', 'TAN', 'THA', 'TLS', 'TOG', 'TGA', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV', 'UGA', 'UKR', 'EUN', 'UAE', 'UAR', 'USA', 'ISV', 'URU', 'UZB', 'VAN', 'VEN', 'VIE', 'FRG', 'WIF', 'YEM', 'YUG', 'ZAM', 'ZIM']
country_url = 'https://www.sports-reference.com/olympics/countries/USA'
athlete_list = []
def country_scraper(country_url):
    page = requests.get(country_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    info = soup.find('div', id = 'info_box')
    try:
        paragraph = info.find_all('p')
        box = paragraph[2].text
        box_split = box.split(': ')
        athlete = box_split[4]
        athlete = athlete.strip(' \n\r\t')
        athlete_list.append(athlete)
    except:
        pass
for country in countries:
    url = 'https://www.sports-reference.com/olympics/countries/' + str(country)
    country_scraper(url)
print(len(countries))
country_scraper(country_url)
print(athlete_list)
def write_csv(countries):
    csvfile = open('athletes.csv', 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow( ['athlete_name'] )
    for athlete in athlete_list:
        c.writerow([athlete])
        url = 'https://www.sports-reference.com/olympics/countries/' + str(countries)
        fill = country_scraper(url)
    csvfile.close()
write_csv(countries)
