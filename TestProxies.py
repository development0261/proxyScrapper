keywords = ['flask','BMW','Django','AUDI','TATA','JAVA','Spring','BridgeStone','Apple','Oneplus','MI','Lenovo','Dell','Macbook','What is ORM','What is OOPS']
ipsfile = open('proxies.txt','r')
ips = [line.replace("\n","") for line in ipsfile.readlines()]
print(ips)
import os,requests

if not os.path.exists("outputfiles/"):
    os.mkdir("outputfiles")

def checkOutputAndStore():
    for keyword in keywords:
        proxies = {'http':ips[0]}
        try:
            response = requests.get("https://google.com/search?q={}".format(keyword), proxies=proxies)
            outputfile = open('outputfiles/{}.html'.format(str(keyword).replace(" ","_")),'w')
            outputfile.write(response.text)
            
        except Exception as e:
            print(e)

checkOutputAndStore()