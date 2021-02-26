import pandas as pd

all = pd.read_csv('all_players.csv')
name_ref = pd.read_csv('./baseballdatabank-master/core/people.csv', index_col='bbrefID')

for i in range(0, len(all['player_ID'])):
    full = name_ref.loc[all['player_ID'][i], ['nameFirst', 'nameLast']]
    full = full['nameFirst'] + ' ' + full['nameLast']
    all['name_common'][i] = full

all.to_csv('all_players.csv', index=None)