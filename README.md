# BaseballWARvContracts

Data Science Final Project on Baseball Player WAR and its relation to their contract

## Project Overview

There are many different metrics to measure how good or valuable a baseball player is throughout a season. One such metric is Wins Above Replacement or WAR. 

WAR is an attempt by the sabermetric baseball community to summarize a player’s total contributions to their team in one statistic. You should always use more than one metric at a time when evaluating players, but WAR is all-inclusive and provides a useful reference point for comparing players. 

WAR offers an estimate to answer the question, “If this player got injured and their team had to replace them with a freely available minor leaguer or a [AAAA player](https://www.baseball-reference.com/bullpen/AAAA_player) from their bench, how much value would the team be losing?” 

This value is expressed in a wins format, so we could say that Player X is worth +6.3 wins to their team while Player Y is only worth +3.5 wins, which means it is highly likely that Player X has been more valuable than Player Y.

Now that we have a general understanding of WAR, that leads up to our project objective and hypothesis. 


## Objective

How does an well-established ('well established' meaning a player has been rewarded a contract of at least 3 years in length) baseball player's WAR move (increases/decreases/stay the same) in relation to completion of their multi-year contract? 

## Why did we select this topic? 

We want our fantasy baseball teams to perform better and that comes through identifying which set of players may be due for a good statistical year based on being within their walk year. That, and also it's fascinating to see how a player performs throughout a season and see how intrinsic value produced in the current year can have them produce at a higher level could lead to a better payday for many seasons to follow. 
But yeah, bottom line - we want our fantasy teams to perform better.

## Hypothesis (question(s) we hope to answer with the data)

We believe that most baseball player's WAR will be at its peak towards the end of their contract because it's so that players can maximize their value for their next potential contract.

## Communication Methods

For this project we are using Discord as a means to centralize information shared and facilitate group video calls. 
Our group has agreed upon to meet during class times and at least one weekend day for review. 

## Resources

(I just added everything from the discord. Let me know what we can remove. Also, I could use some help knowing what was pulled from each source for our dataset).  

* WAR definition - https://library.fangraphs.com/misc/war/ 
* https://community.fangraphs.com/on-war-its-linearity-and-efficient-free-agent-contracts/
* How WAR is calculated - https://www.instructables.com/Calculating-the-WAR-Statistic/#:~:text=The%20formula%20itself%20is%20not,are%20more%20difficult%20to%20calculate.
* mlb-war-data-historical.csv 
* https://community.fangraphs.com/on-war-its-linearity-and-efficient-free-agent-contracts/
* batter.csv
* pitcher.csv
* http://www.stevetheump.com/Payrolls.htm
* http://www.thebaseballcube.com/topics/payrolls/

### Programs used

* PyCharm (Python 3.8.5)
* Jupyter Notebook 


## Final Data Files 

* Current dataset for our analysis: all_players.csv 
* Factoring for inflation by year: Inflation_Constants.csv


## Creating our Dataset

Below is a list of the data columns we came up with and the scripts used to mine it. We narrowed certain criteria of the data we collected as follows: 

We chose to only examine baseball seasons from  1995 to 2019. We chose 1995 as a staring point as there was a baseball strike the previous year, and 2019 as our ending point because of the 2020 Covid-19 pandemic. Both those years if included we believe would have skewed our findings. 

For window of contract, we agreed upon a minimun of 3 years. 

We also only wanted to include a player if they played at least 20% of season to avoid potentially skewed WAR_PSP values.  

#### Columns List 

* Age
* Year
* Team
* League (American League or National League) 
* Player_Salary
* Percent_Season_Played
* WAR_PSP (Wins Above Replacement adjusted for Percentage of Season Played)
* Num_DL_Movements (Number of times in a season player moved to Disabled List) 
* Team_Win_Percentage
* Team_Payroll
* Percent_Contract_Complete

#### Python scripts used for cleaning of data with descriptions, alphabatized 

* Adjusted_WAR_Combining.py - Adjusting the WAR and combining team names
* Cleaning.py - Cleaning the original dataset
* Combining.py - Combing the original dataset into all_players.csv
* Final_Formating.py - Final formatting of the data
* Naming.py - Fixing Mojibake
* Scraping_Contracts.py - Scraping contract data
* Scraping_DL.py - Scraping and adding DL trip data
* Team_Payroll.py - Adding a column for adjusted team payroll
* Team_Wins.py - Adding column for team win percentage

## Machine Learning Model 

* WAR_MLmodel.ipynb

## Dashboard
- Interactive webpage - using the belly button challenge code as a base
- correlation matrices - to display data for WAR in relation to % contract remaining
- Histogram charts
- parallax html
