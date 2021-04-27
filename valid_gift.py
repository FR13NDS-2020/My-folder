import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
line = 0
list = 0
def parse():
    b = open('http.txt').readlines()[line]
    proxy = 'http://' + b
    print(proxy)
    user = UserAgent().random
    headers = {'user_agent': user}
    file = open('test.txt', 'a')
    a = open('discord_gift.txt').readlines()[line]
    url = a
    req = requests.get(url, headers=headers, proxies={'http' : proxy})
    src = req.text
    print(src)
    print(user)
    #print(str(line) + ': ' + a)
    s = req.status_code
    if s != 404:
        file.write(a + '\n')


# line = line + 1
Cs = input('Cheslo strok --->')

while line <= int(Cs):
    parse()
    line = line + 1
    if (line % 2) != 0:
        time.sleep(3)
