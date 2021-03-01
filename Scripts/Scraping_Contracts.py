import pandas as pd
import requests
from lxml import html

all = pd.read_csv('all_players.csv')

link = 'https://www.spotrac.com/search/results/'

name_prev = ''
bad_names = []
names = []
terms = []

for player in range(0, len(all['name_common'])):
    name = all['name_common'][player]
    print(f'\r{player}/{len(all.name_common)}', end='')
    if name != name_prev:
        try:
            name = name.replace(' ', '-')

            page = requests.get(link + name)
            tree = html.fromstring(page.content)

            elements = tree.find_class('contract-type-years')
        except:
            continue

        for i in range(0, len(elements)):
            try:
                if ((int(elements[i].text[5:]) - int(elements[i].text[0:4])) >= 2) and (int(elements[i].text[0:4]) >= 1995):
                    names.append(name.replace('-', ' '))
                    terms.append(elements[i].text)
            except:
                continue

    name_prev = name.replace('-', ' ')


contracts = {'Names': names, 'Years': terms}
contracts = pd.DataFrame(contracts)

contracts.to_csv('contracts.csv', index=None)
