import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

all_df = pd.read_csv('all_players.csv')
for i in range(0, len(all_df['Percent_Contract_Complete'])):
    if all_df['Percent_Contract_Complete'][i] != 100:
        all_df['Percent_Contract_Complete'][i] += np.random.randint(-100000, 100000)/100000
    else:
        all_df['Percent_Contract_Complete'][i] -= np.abs(np.random.randint(-100000, 100000) / 100000)

all_df.plot(kind='scatter', x='Percent_Contract_Complete', y='WAR_PSP')
plt.show()

x = all_df['Percent_Contract_Complete'].values.reshape(-1, 1)
y = all_df['WAR_PSP'].values.reshape(-1, 1)

mod = LinearRegression()
mod.fit(x, y)
mod_pred = mod.predict(x)
print('R Squared Score is: ', r2_score(y, mod_pred))

mod = RandomForestRegressor()
mod.fit(x, y)
mod_pred = mod.predict(x)
print('R Squared Score is: ', r2_score(y, mod_pred))