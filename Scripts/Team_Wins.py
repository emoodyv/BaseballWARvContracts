import pandas as pd

all = pd.read_csv('all_players.csv')
wins_df = pd.read_csv('team_wins.csv', index_col="Year")

wins_df.drop(columns='BLA')
wins_col = [0] * len(all['team_ID'])

for i in range(0, len(all['team_ID'])):
    if all['team_ID'][i].find('FLA') != -1:
        all['team_ID'][i] = all['team_ID'][i].replace('FLA', 'MIA')
    if all['team_ID'][i].find('TBD') != -1:
        all['team_ID'][i] = all['team_ID'][i].replace('TBD', 'TBR')
    if all['team_ID'][i].find('CAL') != -1:
        all['team_ID'][i] = all['team_ID'][i].replace('CAL', 'LAA')
    if all['team_ID'][i].find('ANA') != -1:
        all['team_ID'][i] = all['team_ID'][i].replace('ANA', 'LAA')
    if all['team_ID'][i].find('MON') != -1:
        all['team_ID'][i] = all['team_ID'][i].replace('MON', 'WSN')
    if len(all['team_ID'][i]) == 3:
        wins_col[i] = wins_df[all['team_ID'][i]][all['year_ID'][i]] / wins_df['G'][all['year_ID'][i]]
    elif len(all['team_ID'][i]) == 7:
        wins_col[i] = ((wins_df[all['team_ID'][i][0:3]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][4:7]][all['year_ID'][i]]) / 2) / wins_df['G'][all['year_ID'][i]]
    elif len(all['team_ID'][i]) == 11:
        wins_col[i] = ((wins_df[all['team_ID'][i][0:3]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][4:7]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][8:11]][all['year_ID'][i]]) / 3) / wins_df['G'][all['year_ID'][i]]
    elif len(all['team_ID'][i]) == 15:
        wins_col[i] = ((wins_df[all['team_ID'][i][0:3]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][4:7]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][8:11]][all['year_ID'][i]] +
                       wins_df[all['team_ID'][i][12:15]][all['year_ID'][i]]) / 4) / wins_df['G'][all['year_ID'][i]]

all['Team_Wins'] = wins_col

all = all[all['year_ID'] != 2020]

all.to_csv('all_players.csv', index=None)