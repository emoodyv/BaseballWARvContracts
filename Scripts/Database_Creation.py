import psycopg2
import pandas as pd
from config import database, user, password, host, port

all = pd.read_csv('all_players.csv')

con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

all.Percent_Season_Played = all.Percent_Season_Played.round(6)
all.WAR_PSP = all.WAR_PSP.round(6)
all.Team_Win_Percentage = all.Team_Win_Percentage.round(6)
all.Team_Payroll = all.Team_Payroll.round(0)
all.Percent_Contract_Complete = all.Percent_Contract_Complete.round(6)

cur = con.cursor()
cur.execute('''CREATE TABLE Players
      (Name VARCHAR NOT NULL,
      Age SMALLINT NOT NULL,
      Year SMALLINT NOT NULL,
      Team VARCHAR(15) NOT NULL,
      League VARCHAR(9) NOT NULL,
      Player_Salary INT NOT NUll,
      Percent_Season_Played REAL NOT NULL,
      WAR_PSP REAL NOT NULL,
      Num_DL_Movements SMALLINT NOT NULL,
      Team_Win_Percentage REAL NOT NULL,
      Team_Payroll INT NOT NULL,
      Percent_Contract_Complete REAL NOT NULL);''')

for i in range(0, len(all['Name'])):
    cur.execute(f'''INSERT INTO Players VALUES ('{all['Name'][i]}', {all['Age'][i]}, {all['Year'][i]}, 
    '{all['Team'][i]}', '{all['League'][i]}', {all['Player_Salary'][i]}, {all['Percent_Season_Played'][i]},
    {all['WAR_PSP'][i]}, {all['Num_DL_Movements'][i]}, {all['Team_Win_Percentage'][i]}, {all['Team_Payroll'][i]},
    {all['Percent_Contract_Complete'][i]});''')

con.commit()
con.close()