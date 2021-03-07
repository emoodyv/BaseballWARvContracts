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
* In the ML_discoveries folder there are screenshots of the findings and changes made while conducting this Machine Learning Model. 

To upload the dataset into our ML notebook, we connected it to a postgres database and pulled the data from tables made through SQL.

Our target variable is "war_psp" which is the column of the dataset that holds each player's war value per season. 
 - this is our target value based on our question because we are looking at how the WAR is increasing or decreasing over the time of a player's contract. 

Throughout the Process of designing this model there were early disoveries made with dimesionality reduction. Through encoding, it was evident that the 167 unique values in the team column of the dataset were not significant enough for our analysis. Therefore we were able to drop the team column from our dataframe. We also set the name column as the index in order to keep it from interefearing with our analysis but keeping it in the dataframe for index values.

The league column was also encoded into values 0, 1, 2 to represent the different leagues, the American League and the National League, as well as one trade instances of players who, mid season, were traded to the other league. We uniformed this case a single value of "AL/NL" in order to reduce variety in our dataset. 

Using R studio, we ran linear regression analyses on different interactions and combinations of the remaining features. This led us to the ACI copmutation step in which we discovered that the lowest AIC is the total combination model. The total combination model consists of all the remaining features: "age", "year", "league", "player_salary", "percent_season_played", "num_dl_movements", "team_win_percentage", "team_payroll", "percent_contract_complete". 

Our model choice is Linear Regression due to its sucecptibility to overfitting and its dimensionality reduction techinques. The disadvantages that come with this model choice is that we are not 100% certain on the relationships between the variables, so assuming the relationships are linear could lead to arising problems within our model. The assumed independence between variables is a disadvantage as there are variables in our dataset that are based on team values when our index is indidually based. 

The results at which we arrived based on the linear regression are that salary and team payroll have the highest p-values meaning they are the least statistically significant variables within this analysis. Thus they are not key elements in our anlaysis on WAR for a player, and can be removed from the dataset. For furthre analysis of this dataset, we are going to clean the current model and continue checking for increased accuracy. 



# Week 2 - Scaffolding Phase 

### Google Slides Dashboard layout v.1 
https://docs.google.com/presentation/d/1sS-l4fdMVWR8aU56O_TnNt9hhm58viymPNDhlr7l34g/edit?usp=sharing

Attached is the very very VERY rough draft of how the dashboard website could look like. I based this based on Jonathan’s index.html + style.css  files that he shared the other day as well as Ed’s Tableau storyboard. 

Ed says that we can embed specific worksheets into an index.html file, so that they can be showcased separately, so that is the concept behind this rough design. We may decide to showcase the data graphs in a different way. 

I do like the idea of using Tableau’s worksheets because it’s easier than creating code from scratch in an index.html file, and all the interactive features would be included. 

### SLIDE 1 
![](https://github.com/Shap3shifter/BaseballWARvContracts/blob/josef-scaffolding/Images%20for%20Google%20Slides%20Scaffolding/1.png)
What people visiting the site would see when first… visiting. I didn’t add any images yet or customize things. Note the clickable links. 

### SLIDE 2
![](https://github.com/Shap3shifter/BaseballWARvContracts/blob/josef-scaffolding/Images%20for%20Google%20Slides%20Scaffolding/2.png)
This site is designed so that  when you click on a link, it scrolls down to that section of the website (similar to a restaurant menu on door dash or something) 

### SLIDE 3
![](https://github.com/Shap3shifter/BaseballWARvContracts/blob/josef-scaffolding/Images%20for%20Google%20Slides%20Scaffolding/3.png)
This would be the first Tableau Worksheet that would be interactive the same way as if it were in a shared tableau link. 

### SLide 4
![](https://github.com/Shap3shifter/BaseballWARvContracts/blob/josef-scaffolding/Images%20for%20Google%20Slides%20Scaffolding/4.png)
The rest of the slides is a scaffolding of the rest of the tableau worksheets displayed on website (each clickable to scroll to). 

### How will Page Interact/Behave? 

1. Adjusted WAR and Salary
	* Our x-axis represents player salary, our y-axis represents players Adjusted WAR.
	* Data points in this graph can be clicked and when clicked, will display:
		* Adjusted WAR 
		* Player Name
		* Player Salary 
		* Year
	* Filters that can the user can utilize to narrow down displayed datapoint
		*  A year data check box filter 
		*  A name search bar
		*  A slide bar filter to narrow down displayed data points by WAR score. 
		*  A slide bar filter to narrow down displayed data points by salary. 

2. Salary in Relation to Age * Our x-axis represents player age, our y-axis represents player salary.
	* Data points in this graph can be clicked and when clicked, will display:
		* Age
		* Player Name
		* Player Salary 
		* Year
	*  Filters that can the user can utilize to narrow down displayed datapoint
		*  Year data check box filter 
		*  A name search bar
		*  A slide bar filter to narrow down displayed data points by WAR score. 
		*  A slide bar filter  to narrow down displayed data points by age. 

3. Team payroll throughout the years  
    * Our x-axis represents year, our y-axis represents team payroll. 
	* Data points in this graph can be clicked and when clicked, will display:
		* Team
		* Team Payroll
		* Year
	*  Filters that can the user can utilize to narrow down displayed datapoint
		*  A Y ear data check box filter 
		* A Team ID data check box filter 
		* A slide bar filter of team payroll 
4. Percent of Season played in relation to Adj. WAR 
	* Our x-axis represents Percent of Season Played, our y-axis represents player adjusted WAR. 
	* Data points in this graph can be clicked and when clicked, will display:
		* % of Season Played
		* Adj. WAR 
		* Player Name
		* Year
	*  Filters that can the user can utilize to narrow down displayed datapoint
		*  A Year data check box filter 
		* A slide bar filter of Adj. WAR
		* A slide bar filter of % of season played
		* A name search bar

### Describe tools used in final dashboard/How page will interact/behave

We are so far using Tableau to create our worksheets that we want to display in a website format through an Index.html file. 

We will either have a single webpage that has our individual worksheets spaced out throughout the length of the webpage, with hyperlinks that auto-scroll you down to that section of the page OR a webpage with hyperlinks that take a user to a sub-page with a specific worksheet. 

### How will users interact with the page?

Users will be able to access the website and it’s data worksheets created in Tableau, and interact with the worksheets by being able to filter specific criteria based on which worksheet they are on. 

### side notes 

Obviously proper descriptions of what each worksheet represents, and how to interact with them should be included in each section. 

Please give some feedback (things that may be missing/need to be included, themes, etc). Ed and I are down to take point for getting this all up and running. 

=======
## Dashboard
- Interactive webpage - using the belly button challenge code as a base
- correlation matrices - to display data for WAR in relation to % contract remaining
- Histogram charts
- parallax html

