import pandas as pd
import requests
import pathlib
import bs4
import csv
import sys

i = 1
url = 'http://www.vgchartz.com/games/games.php?page=' + str(i) + '&results=50&name=&console=NS&keyword=&publisher=&genre=&order=Sales&ownership=Both&boxart=Both&banner=Both&showdeleted=&region=All&goty_year=&developer=&direction=DESC&showtotalsales=0&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1&alphasort=&showmultiplat=No'
for i in range(2):
    i = i+1
    res = requests.get(url)
    res.raise_for_status()
    #determine if the requests object is created successfully

    ns_html_file = open('nintendo_switch_game_rankings.txt', 'wb')
    for chunk in res.iter_content(100000):
        ns_html_file.write(chunk)
        print('chunks')
    ns_html_file.close()
    print('done {}'.format(i))
    url = 'http://www.vgchartz.com/games/games.php?page=' + str(i) + '&results=50&name=&console=NS&keyword=&publisher=&genre=&order=Sales&ownership=Both&boxart=Both&banner=Both&showdeleted=&region=All&goty_year=&developer=&direction=DESC&showtotalsales=0&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1&alphasort=&showmultiplat=No'
    #create a local copy of HTML ranking page at URL in line 9

soup_file_prep = open('nintendo_switch_game_rankings.txt')
ns_file_soup = bs4.BeautifulSoup(soup_file_prep, features='lxml')
#convert downloaded HTML to bs object

ns_game_titles = open('ns_game_names.csv', 'w')
for i in ns_file_soup.select('a[href^="http://www.vgchartz.com/game/"]'):
    ns_game_titles.write(i.text + '\n')
ns_game_titles.close()
#write game names to a csv file

df = pd.read_csv('ns_game_names.csv',
                 sep='\n',
                 encoding = 'ISO-8859-1',
                 header=None,
                 names=['Game Titles'])
#https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python for solving encoding error

print(df)
