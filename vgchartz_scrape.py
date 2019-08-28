import bs4
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
