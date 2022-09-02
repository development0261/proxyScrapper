import requests
from bs4 import BeautifulSoup
import csv
import urllib3

def checkifProxyWorking(randomIp):
    import requests
    proxies = {}
    print(randomIp)
    if randomIp['is_https'] == "yes":
        proxies['https'] = "https://{}:{}".format(randomIp['ip'],randomIp['port'])
    else:
        proxies['http'] = "http://{}:{}".format(randomIp['ip'],randomIp['port'])
    try:
        response = requests.get("https://google.com/search?q=django", proxies=proxies)
        return True
    except:
        return False


URL = "https://free-proxy-list.net/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
proxyTable = soup.findAll('div', attrs = {'class':'fpl-list'})
proxyBody = proxyTable[0].find('tbody')
rows = proxyBody.find_all('tr')
proxiesList = []
f = open('proxies.txt', 'w')
for row in rows[:50]:
    data = row.find_all("td")
    if data[5].get_text() == "yes":
        proxiesList.append({
            "ip":data[0].get_text(),
            "port":data[1].get_text(),
            "code":data[2].get_text(),
            "google":data[5].get_text(),
            "is_https":data[6].get_text(),
        })
        if data[6].get_text() == "yes":
            resp = checkifProxyWorking({
                "ip":data[0].get_text(),
                "port":data[1].get_text(),
                "code":data[2].get_text(),
                "google":data[5].get_text(),
                "is_https":data[6].get_text(),
            })
            if resp:
                f.write("https://{}:{}".format(data[0].get_text(),data[1].get_text()))
                f.write("\n")
           
        else:
            resp = checkifProxyWorking({
                "ip":data[0].get_text(),
                "port":data[1].get_text(),
                "code":data[2].get_text(),
                "google":data[5].get_text(),
                "is_https":data[6].get_text(),
            })
            if resp:
                f.write("http://{}:{}".format(data[0].get_text(),data[1].get_text()))
                f.write("\n")
f.close()

