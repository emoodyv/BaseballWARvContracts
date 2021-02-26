import pandas as pd

bat = pd.read_csv('batter.csv', index_col=False)
pit = pd.read_csv('pitcher.csv', index_col=False)

PSPF_P = 187
PSPF_B = 683.64

bat['%SP'] = bat['PA'] / PSPF_B
pit['%SP'] = pit['IP'] / PSPF_P

bat['adj_WAR'] = bat['WAR'] / bat['%SP']
pit['adj_WAR'] = pit['WAR'] / pit['%SP']

bat = bat.drop(columns=['PA', 'G'])
pit = pit.drop(columns=['G', 'GS', 'IP'])

all = bat.append([pit])

all.groupby('player_ID')

col_to_drop = []
i = 0
j = 0
print(all['year_ID'][i])

for i in range(0, len(all['year_ID']) - 1):
    if (all['year_ID'][i] == all['year_ID'][i+1]) and (all['player_ID'][i] == all['player_ID'][i+1]):
        all['team_ID'][i] = all['team_ID'][i] + '/' + all['team_ID'][i+1]
        if all['lg_ID'][i] != all['lg_ID'][i+1]:
            all['lg_ID'][i] = all['lg_ID'][i] + '/' + all['lg_ID'][i + 1]
        for name in ['WAR', '%SP']:
            all[name][i] = all[name][i] + all[name][i+1]
        all['salary'][i] = all['salary'][i+1]
        col_to_drop.append(i+1)
    try:
        if (all['year_ID'][i] == all['year_ID'][i + 2]) and (all['player_ID'][i] == all['player_ID'][i + 2]):
            all['team_ID'][i] = all['team_ID'][i] + '/' + all['team_ID'][i + 2]
            if all['lg_ID'][i] != all['lg_ID'][i + 2]:
                all['lg_ID'][i] = all['lg_ID'][i] + '/' + all['lg_ID'][i + 2]
            for name in ['WAR', '%SP']:
                all[name][i] = all[name][i] + all[name][i + 2]
            all['salary'][i] = all['salary'][i + 2]
            col_to_drop.append(i + 2)
        elif (all['year_ID'][i] == all['year_ID'][i + 3]) and (all['player_ID'][i] == all['player_ID'][i + 3]):
            all['team_ID'][i] = all['team_ID'][i] + '/' + all['team_ID'][i + 3]
            if all['lg_ID'][i] != all['lg_ID'][i + 3]:
                all['lg_ID'][i] = all['lg_ID'][i] + '/' + all['lg_ID'][i + 3]
            for name in ['WAR', '%SP']:
                all[name][i] = all[name][i] + all[name][i + 3]
            all['salary'][i] = all['salary'][i + 3]
            col_to_drop.append(i + 3)
    except:
        continue

all['adj_WAR'] = all['WAR'] / all['%SP']

all = all.drop(all.index[col_to_drop])

all = all[all['%SP'] >= .2]

all.to_csv('all_players.csv', index=None)