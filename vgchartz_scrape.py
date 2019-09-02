import pandas as pd
import requests
import pathlib
import bs4
import csv
import sys

res = requests.get('http://www.vgchartz.com/gamedb/games.php?console=NS')
res.raise_for_status()
#determine if the requests object is created successfully
ns_html_file = open('nintendo_switch_game_rankings.txt', 'wb')
for chunk in res.iter_content(100000):
    ns_html_file.write(chunk)
ns_html_file.close()
#create a local copy of HTML ranking page at URL in line 7
soup_file_prep = open('nintendo_switch_game_rankings.txt')
ns_file_soup = bs4.BeautifulSoup(soup_file_prep, features='lxml')
#convert downloaded HTML to bs object
ns_game_titles = open('ns_game_names.csv', 'w')
for i in ns_file_soup.select('a[href^="http://www.vgchartz.com/game/"]'):
    ns_game_titles.write(i.text + '\n')
ns_game_titles.close()
#write game names to a csv file
df = pd.read_csv('ns_game_names.csv', sep='\n', encoding = 'ISO-8859-1')
#https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python for solving encoding error
print(df.head())
