import bs4
import pandas as pd
import requests
import pathlib
import bs4

res = requests.get('http://www.vgchartz.com/gamedb/games.php?console=NS')
res.raise_for_status()
#determine if the requests object is created successfully
