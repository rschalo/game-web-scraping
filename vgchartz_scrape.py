import pandas as pd
import requests
import pathlib
import bs4

res = requests.get('http://www.vgchartz.com/gamedb/games.php?console=NS')
res.raise_for_status()
#determine if the requests object is created successfully
ns_html_file = open('nintendo_switch_game_rankings', 'wb')
for chunk in res.iter_content(100000):
    ns_html_file.write(chunk)
ns_html_file.close()
#create a local copy of HTML ranking page at URL in line 7
soup_file_prep = open('nintendo_switch_game_rankings')
ns_file_soup = bs4.BeautifulSoup(soup_file_prep, features='lxml')
#convert downloaded HTML to bs object
ns_game_titles = open('ns_game_names', 'w')
for i in ns_file_soup.select('a[href^="http://www.vgchartz.com/game/"]'):
    ns_game_titles.write(i.text + '\n')
ns_game_titles.close()
#write game names to a file
