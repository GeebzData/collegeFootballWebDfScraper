# College Football Data Web Scraper
This python script iterates through 2015-2018 Penn State Football season offensive data, writes it all to one DataFrame, and exports a csv with the data. This script can be changed to reflect any number of seasons and any team that Sports Reference has.

https://www.sports-reference.com/cfb/schools/

This file can be edited to fit different needs:
* To change the year edit lines 11 & 18 range value to be 201{range(x,y)}
```
2015-2017
for i in range(5,8):

e.g. 2010-2012
for i in range(0,3):
```
```
For years before 2010, the read variable will need to be edited
e.g. for 2006-2008
read = pd.read_html('https://www.sports-reference.com/cfb/schools/penn-state/201{}/gamelog/'.format(i), header=0)
>>
for i in range(6,9):
read = pd.read_html('https://www.sports-reference.com/cfb/schools/penn-state/200{}/gamelog/'.format(i), header=0)
```
* To edit the team, change the url to reflect the team data wanted
```
https://www.sports-reference.com/cfb/schools/penn-state/2017/gamelog/

e.g. - change to alabama data
https://www.sports-reference.com/cfb/schools/alabama/2017/gamelog/
```
