#!/opt/homebrew/bin/python3

import urllib.request
from bs4 import BeautifulSoup

fp = urllib.request.urlopen("https://sportsgamestoday.com/tv/what-to-watch.php")
mybytes = fp.read()

content = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(content, 'html.parser')
sp0rts = []
for a in soup.find_all('table'):
    for x in a.find('th', 'wtwmatchuptitle'):
        print('CATEGORY: ' + x)
    for y in a.find('td', 'wtwmatchup'):
        print('EVENT: ' + y)
    for z in a.find('td', 'wtwtime'):
        print('TIME: ' + z)
    for tv in a.find('td', 'wtwtvchannel'):
        print('TV: ' + tv.text)
