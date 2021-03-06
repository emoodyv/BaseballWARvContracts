import psycopg2
import pandas as pd
from config import database, user, password, host, port

all_df = pd.read_csv('all_players.csv')

all_df.Percent_Season_Played = all_df.Percent_Season_Played.round(6)
all_df.WAR_PSP = all_df.WAR_PSP.round(6)
all_df.Team_Win_Percentage = all_df.Team_Win_Percentage.round(6)
all_df.Team_Payroll = all_df.Team_Payroll.round(0)
all_df.Percent_Contract_Complete = all_df.Percent_Contract_Complete.round(6)

pcc = all_df['Percent_Contract_Complete']
all_df = all_df.drop(columns=['Percent_Contract_Complete'])

con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

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
      Team_Payroll INT NOT NULL);''')

cur.execute('''CREATE TABLE Results(
      Percent_Contract_Complete REAL NOT NULL);''')

for i in range(0, len(all_df['Name'])):
    cur.execute(f'''INSERT INTO Players VALUES ('{all_df['Name'][i]}', {all_df['Age'][i]}, {all_df['Year'][i]}, 
    '{all_df['Team'][i]}', '{all_df['League'][i]}', {all_df['Player_Salary'][i]}, {all_df['Percent_Season_Played'][i]},
    {all_df['WAR_PSP'][i]}, {all_df['Num_DL_Movements'][i]}, {all_df['Team_Win_Percentage'][i]}, {all_df['Team_Payroll'][i]});''')

for i in range(0, len(pcc)):
    cur.execute(f'''INSERT INTO Results VALUES ({pcc[i]});''')

con.commit()

cur.execute('''SELECT * FROM Players CROSS JOIN Results ;''')
cur.execute('''DROP TABLE Results;''')

con.commit()
con.close()