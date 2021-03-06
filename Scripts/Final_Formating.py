import pandas as pd

all = pd.read_csv('all_players.csv')
contracts = pd.read_csv('contracts.csv')
inflation = pd.read_csv('Inflation_Constants.csv', index_col='Year')

names = []
terms = []
pcc = []
Percent_Contract_Complete = [0] * len(all['name_common'])

for i in range(0, len(contracts)):
    for j in range(int(contracts['Years'][i][0:4]), int(contracts['Years'][i][5:]) + 1):
        length_temp = int(contracts['Years'][i][5:]) - int(contracts['Years'][i][0:4]) + 1
        names.append(contracts['Names'][i])
        terms.append(j)
        pcc.append(((j - int(contracts['Years'][i][0:4]) + 1)/length_temp) * 100)

contracts = {'Names': names, 'Years': terms, 'Percent': pcc}
contracts = pd.DataFrame(contracts)

for i in range(0, len(all['name_common'])):
    print(f'\r{i}/{len(all.name_common)}', end='')
    for j in range(0, len(contracts['Names'])):
        if all['name_common'][i] == contracts['Names'][j] and all['year_ID'][i] == contracts['Years'][j]:
            Percent_Contract_Complete[i] = contracts['Percent'][j]

all['Percent_Contract_Complete'] = Percent_Contract_Complete
all = all[all['Percent_Contract_Complete'] != 0]

all = all.drop(columns=['player_ID', 'WAR'])
all = all.rename(columns={'name_common': 'Name', 'age': 'Age', 'year_ID': 'Year', 'team_ID': 'Team', 'lg_ID': 'League',
                          'salary': 'Player_Salary', '%SP': 'Percent_Season_Played', 'adj_WAR': 'WAR_PSP',
                          'DL_Trips': 'Num_DL_Movements', 'Team_Wins': 'Team_Win_Percentage'})

for i in range(0, len(all['Name'])):
    conv = inflation.loc[(all['Year'][i])]
    all['Player_Salary'][i] = all['Player_Salary'][i] * conv

all.to_csv('all_players.csv', index=None)