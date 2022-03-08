from autoscraper import AutoScraper
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

scraper = AutoScraper()
url = "https://www.vlr.gg/stats/?min_rating=1800&agent=all&map_id=all&timespan=all"
scraper.build(url, ["mwzera", "267.2"])
data = scraper.get_result_similar(url, grouped=True)
data = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in data.items()]))
data = data.rename({data.columns.values[0]:'player', data.columns.values[1]:'ACS'}, axis=1)

ages = [] 
earnings = []
for player in data['player'].tolist():
    player_url = "https://liquipedia.net/valorant/" + player
    req = requests.get(player_url, headers={'useragent': 'Statistics Project / ethan.yu22@bcp.org)', 'Accept-Encoding': 'gzip'}, timeout=(10, None))
    if req.status_code != 404:
        soup = BeautifulSoup(req.content, 'html.parser')
        age = soup.find_all('span', class_='noprint')
        if soup.find('div', text='Approx. Total Earnings:', class_='infobox-cell-2') == None:
            earning = None
        else:
            earning = soup.find('div', text='Approx. Total Earnings:', class_='infobox-cell-2').find_next('div').string
        if len(age) == 0:
            ages.append(None)
            age = "None"
        else:
            age = age[0].string
            age = re.sub("[^0-9]", "", age)
            ages.append(age)
            age = str(age)
        if earning == None:
            earnings.append(None)
            earning = "None"
        else:
            earnings.append(earning)
        print(str(len(ages)) + ": " + player + ", " + age + ", " + earning)
    else:
        ages.append(None)
        earnings.append(None)
        print(str(len(ages)) + ": " + player + ", NULL")
    time.sleep(30.1)
for earning in earnings:
    if earning == None:
        continue
    earning = type(int(earning[1:].replace(',','')))
for age in ages:
    if age == None:
        continue
    age = int(age)
data['age'] = ages
data['earnings'] = earnings
data.to_csv('data.csv')
                
