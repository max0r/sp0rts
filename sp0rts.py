#!/usr/bin/env python3

import urllib.request
from collections import OrderedDict
from bs4 import BeautifulSoup
from tabulate import tabulate

emojis = {
    'MLB' : '⚾️',
    'NBA' : '🏀'
        }

fp = urllib.request.urlopen("https://sportsgamestoday.com/tv/what-to-watch.php")
mybytes = fp.read()

content = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(content, 'html.parser')
sp0rts = []
print('sp0rts:')
for a in soup.find_all('table'):
    event = OrderedDict()
    for x in a.find('th', 'wtwmatchuptitle'):
        event['category'] = x
        event['icon'] = emojis.get(x)
    for y in a.find('td', 'wtwmatchup'):
        event['title'] = y.strip()
    for z in a.find('td', 'wtwtime'):
        event['time'] = z
    event['chans'] = []
    for tv in a.find('td', 'wtwtvchannel'):
        if tv.find('br'):
            event['chans'].append(tv)
    sp0rts.append(event)
print(tabulate(sp0rts, tablefmt='github'))
