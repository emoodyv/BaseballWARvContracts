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

all.to_csv('all_players.csv', encoding='latin-1', index=None)