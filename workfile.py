import requests
line = 0

def chek():
    a = open('http.txt').read().split('\n')[line]
    proxy = 'http://' + str(a)
    file = open('valid_proxy_https.txt', 'a')
    r = requests.get('https://httpbin.org/ip', proxies={'http': proxy}, timeout=2)
    code = r.status_code
    print(code)
    if code == 200:
        file.write(a + '\n')

Cs = input('Cheslo strok --->')

while line <= int(Cs):
    chek()
    line = line + 1
