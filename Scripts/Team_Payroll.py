import pandas as pd
from selenium import webdriver as wd

all = pd.read_csv('all_players.csv')
inflation_constants = pd.read_csv('Inflation_Constants.csv', index_col='Year')

options = wd.ChromeOptions()
options.add_experimental_option("detach", True)
driver = wd.Chrome(options=options)
driver.implicitly_wait(1)

conversion = {'Arizona Diamondbacks': 'ARI', 'Atlanta Braves': 'ATL', 'Baltimore Orioles': 'BAL',
              'Boston Red Sox': 'BOS', 'Chicago Cubs': 'CHC', 'Chicago White Sox': 'CHW', 'Cincinnati Reds': 'CIN',
              'Cleveland Indians': 'CLE', 'Colorado Rockies': 'COL', 'Detroit Tigers': 'DET', 'Houston Astros': 'HOU',
              'Kansas City Royals': 'KCR', 'California Angels': 'LAA', 'Los Angeles Angels of Anaheim': 'LAA',
              'Los Angeles Angels': 'LAA', 'Anaheim Angels': 'LAA', 'Los Angeles Dodgers': 'LAD',
              'Florida Marlins': 'MIA', 'Miami Marlins': 'MIA', 'Milwaukee Brewers': 'MIL', 'Minnesota Twins': 'MIN',
              'New York Mets': 'NYM', 'New York Yankees': 'NYY', 'Oakland Athletics': 'OAK',
              'Philadelphia Phillies': 'PHI', 'Pittsburgh Pirates': 'PIT', 'San Diego Padres': 'SDP',
              'San Francisco Giants': 'SFG', 'Seattle Mariners': 'SEA', 'St. Louis Cardinals': 'STL',
              'Tampa Bay Devil Rays': 'TBR', 'Tampa Bay Rays': 'TBR', 'Texas Rangers': 'TEX',
              'Toronto Blue Jays': 'TOR', 'Washington Nationals': 'WSN', 'Montreal Expos': 'WSN'}

payroll_col = [0] * len(all['team_ID'])

for i in range(1995, 2020):
    driver.get('http://www.thebaseballcube.com/topics/payrolls/byYear.asp?Y=' + str(i))
    element = driver.find_element_by_xpath('//*[@id="gridTotalCount1"]').get_attribute('textContent')
    num_teams = int(element[0:2])
    team = []
    payroll = []
    for j in range(0, num_teams):
        team.append(driver.find_element_by_xpath('//*[@id="grid1"]/tbody/tr[' +
                                                  str(j+2) + ']/td[2]/a').get_attribute('textContent'))
        payroll.append(driver.find_element_by_xpath('//*[@id="grid1"]/tbody/tr[' +
                                                    str(j+2) + ']/td[5]/a').get_attribute('textContent'))
    for j in range(0, len(team)):
        team[j] = conversion[team[j]]

    combined = {team[k]: payroll[k] for k in range(len(team))}

    for j in range(0, len(all['team_ID'])):
        if all['year_ID'][j] == i and len(all['team_ID'][j]) == 3:
            payroll_col[j] = float(combined[all['team_ID'][j]].replace(',','')) * float(inflation_constants.loc[i])
        elif all['year_ID'][j] == i and len(all['team_ID'][j]) == 7:
            payroll_col[j] = ((float(combined[all['team_ID'][j][0:3]].replace(',','')) +
                               float(combined[all['team_ID'][j][4:7]].replace(',',''))) / 2) * \
                               float(inflation_constants.loc[i])
        elif all['year_ID'][j] == i and len(all['team_ID'][j]) == 11:
            payroll_col[j] = ((float(combined[all['team_ID'][j][0:3]].replace(',', '')) +
                               float(combined[all['team_ID'][j][4:7]].replace(',', '')) +
                               float(combined[all['team_ID'][j][8:11]].replace(',', ''))) / 3) * \
                               float(inflation_constants.loc[i])
        elif all['year_ID'][j] == i and len(all['team_ID'][j]) == 15:
            payroll_col[j] = ((float(combined[all['team_ID'][j][0:3]].replace(',', '')) +
                               float(combined[all['team_ID'][j][4:7]].replace(',', '')) +
                               float(combined[all['team_ID'][j][8:11]].replace(',', '')) +
                               float(combined[all['team_ID'][j][12:15]].replace(',', ''))) / 4) * \
                               float(inflation_constants.loc[i])

all['Team_Payroll'] = payroll_col

all.to_csv('all_players.csv', index=None)