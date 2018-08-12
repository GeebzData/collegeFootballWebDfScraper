import csv
import pandas as pd

# create column headers for final df
col = ['Game Number', 'Date', 'Location', 'Opponent', 'Result', 'Passing Completion', 'Passing Attempts', 'Passing Percentage', 'Passing Yards', 'Passing TDs', 'RushingA ttempts', 'Rushing Yards', 'Rushing Average', 'Rushing TDs', 'Offensive Plays', 'Offensive Yards', 'Offensive Average', 'First Down Pass', 'First Down Rush', 'First Down Penalties', 'First Down Total', 'Penalties', 'Penalty Yards', 'Fumbles', 'Interceptions', 'Total Turnovers']

# iterate over web pages from years 2015-2018, once past 2015, move to the else statement
for i in range(5,8):
# iterate through first web page to pull the offensive df
    if i == 5:
        psu = pd.read_html('https://www.sports-reference.com/cfb/schools/penn-state/201{}/gamelog/'.format(i), header=0)
        # select first df on page and remove bottom row and header
        psu_season = psu[0].iloc[1:-1:]
        # create header - col
        psu_season.columns = col
# iterate through every other web page to pull the offensive df
    else:
        psu = pd.read_html('https://www.sports-reference.com/cfb/schools/penn-state/201{}/gamelog/'.format(i), header=0)
        psu_season_data = psu[0].iloc[1:-1:]
        psu_season_data.columns = col
        # concat original & appended df with new df
        psu_season = pd.concat([psu_season, psu_season_data])

# the row value indicates how many games were played, it should result in 26 columns
print(psu_season.shape)

#-- export df to a csv
psu_season.to_csv('/PATH/PSU.csv')
