import pandas as pd
from selenium import webdriver as wd
import numpy as np

all = pd.read_csv('all_players.csv')

options = wd.ChromeOptions()
options.add_experimental_option("detach", True)
driver = wd.Chrome(options=options)
driver.implicitly_wait(1)

def dl_finder():
    temp_names_on = []
    temp_names_off = []
    temp_year = []
    num_pages = 917
    for page in range(0, num_pages):
        try:
            driver.get('http://www.prosportstransactions.com/baseball/Search/SearchResults.php?Player=&Team='
                       '&BeginDate=1995-01-01&EndDate=2021-02-23&DLChkBx=yes&submit=Search&start=' + str(page*25))
            for i in range(2, 27):
                element_name = driver.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[' + str(i) + ']/td[4]')
                temp_names_on.append(element_name.get_attribute('textContent'))
                element_name = driver.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[' + str(i) + ']/td[3]')
                temp_names_off.append(element_name.get_attribute('textContent'))
                element_name = driver.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[' + str(i) + ']/td[1]')
                temp_year.append(element_name.get_attribute('textContent'))
        except:
            print('Error')
        print("Scraping page #" + str(page + 1))
    dl_trips = np.empty(shape=(len(temp_year), 3), dtype='object')
    for i in range(0, len(temp_year)):
        dl_trips[i][0] = temp_year[i]
        if len(temp_names_on[i]) < len(temp_names_off[i]):
            dl_trips[i][1] = temp_names_off[i]
            dl_trips[i][2] = 'off'
        else:
            dl_trips[i][1] = temp_names_on[i]
            dl_trips[i][2] = 'on'
    return dl_trips


dl_trips = np.array(dl_finder())
dl_col = [0] * len(all['name_common'])
all['DL_Trips'] = dl_col
dl_trips = dl_trips[~np.any(dl_trips == "off", axis=1)]

for i in range(0, len(all['name_common'])):
    for j in range(0, dl_trips.shape[0]):
        if str(all['name_common'][i]) in str(dl_trips[j][1]) and str(all['year_ID'][i]) in str(dl_trips[j][0]):
            all['DL_Trips'][i] += 1

all.to_csv('all_players.csv', index=None)