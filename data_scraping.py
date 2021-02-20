# Packages for Web-Scraping
from requests import get
from bs4 import BeautifulSoup
from time import time
from time import sleep
from random import randint
from warnings import warn

# Packages for Saving File after Scraping
import numpy as np
import pandas as pd

pages = 5

statement = []
link = []
veracity = []

for i in range(0, pages):
    response = get(f'https://www.politifact.com/factchecks/list/?page={i}&category=truth-o-meter')

    # Sleep, so IP address does not get banned
    sleep(randint(8,15))

    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(i, response.status_code))

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    statement_containers = html_soup.find_all('div', class_ = 'm-statement__content')

    # Extract data from individual container
    for container in statement_containers:
        sta = container.find('a').get_text(strip=True)
        statement.append(sta)

        lin = container.find('a')["href"]
        link.append(lin)

        ver = container.find('img')

        if ver == None: break

        veracity.append(ver['alt'])

dataset = pd.DataFrame(
    {'statement': statement,
    'link': link,
    'veracity': veracity
})
dataset.to_csv('dataset.csv')