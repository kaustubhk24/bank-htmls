import urllib.request
import bs4

import requests

from bs4 import BeautifulSoup
opener = urllib.request.FancyURLopener({})
url = "https://bank-details.swayalgo.com/"

 
 
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
i=0
for link in soup.find_all('a'):
    i+=1
    link=str("https://bank-details.swayalgo.com/"+str(link.get('href')))
    print(str(i)+link)
    if i<50000:
        fiel=open('sitemap.txt','a')
    elif i<100000:
        fiel=open('sitemap1.txt','a')
    elif i<150000:
        fiel=open('sitemap2.txt','a')
    elif i<200000:
        fiel=open('sitemap3.txt','a')
    elif i<250000:
        fiel=open('sitemap4.txt','a')
    elif i<300000:
        fiel=open('sitemap5.txt','a')
    fiel.write("\n")
    fiel.write(link)


