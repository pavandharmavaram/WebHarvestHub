from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup


def crr(request):
    return render(request,"index.html")



url="https://www.bikewale.com/bajaj-bikes/"
resp=requests.get(url)
#print(resp)

sop=BeautifulSoup(resp.content,'html.parser');
#print(sop)
link=sop.find_all('div',class_="o-fznJEv o-bTDyCI o-brXWGL")
links=[]
for i in link[0:20]:
    n="https://www.bikewale.com/"+i.a['href']
    links.append(n)
#print(namess)

name=sop.find_all('h3',class_="o-jjpuv o-cVMLxW o-mHabQ o-fzpibK")
names=[]

for i in name[0:20]:
    k=i.get_text()
    names.append(k)
#print(names)

image=sop.find_all('img',class_="o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI")

images=[]

for i in image[0:20]:
    k=i['src']
    images.append(k)
#print(images)

price=sop.find_all('span',class_="o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT")
prices=[]

for i in price[0:20]:
    k=i.get_text()
    prices.append(k)
#print(prices)

rating=sop.find_all('p',class_="o-frVjwE o-bdcqVx o-cKuOoN o-lIIwF o-eZTujG")
ratings=[]

for i in rating[0:20]:
    k=i.get_text()
    ratings.append(k)
#print(ratings)

mylist=zip(links,images,names,prices,ratings)

#print(mylist)
def bajaj(request):
    return render(request,"bajaj.html",{ 'mylist':mylist})





url1="https://www.amazon.in/gp/most-gifted/electronics/1389432031?ref_=Oct_d_omg_S&pd_rd_w=MBtRJ&content-id=amzn1.sym.006ee841-3675-4c65-aeb6-21aca28b9942&pf_rd_p=006ee841-3675-4c65-aeb6-21aca28b9942&pf_rd_r=08TH03NZ8JMXW5VE42FQ&pd_rd_wg=bSwfb&pd_rd_r=06ec3018-6873-4528-8023-65bdbb32123a"
resp1=requests.get(url1)
#print(resp1)

sop1=BeautifulSoup(resp1.content,'html.parser');

iphone=sop1.find_all('img',class_="a-dynamic-image p13n-sc-dynamic-image p13n-product-image")
iphones=[]

for i in iphone:
    k=i['src']
    iphones.append(k)
    
ilink=sop1.find_all('a',class_="a-link-normal")
iplinks=[]

for i in ilink:
    p="https://www.amazon.in/"+i['href']
    iplinks.append(p)


iname=sop1.find_all('div',class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
inames=[]

for i in iname:
    k=i.get_text()
    inames.append(k)
    

iprice=sop1.find_all('div',class_="a-row")
iprices=[]
for i in iprice:
    j=i.span.get_text()
    iprices.append(j)


iphonel=zip(iphones,iplinks,inames,iprices)

def iphone(request):
    return render(request,"hero.html",{'iph':iphonel})


url2="https://www.oppo.com/in/smartphones/"
ram=requests.get(url2)

sop2=BeautifulSoup(ram.content,'html.parser');

oppoimg=sop2.find_all('img', class_="lazyloaded")
oppoimgs=[]

for i in oppoimg:
    k=i['src']
    oppoimgs.append(k)

oppolink=sop2.find_all('div',class_="swiper-wrapper")
oppolinks=[]

for i in oppolink:
    k=i.a['href']
    oppolinks.append(k)

oppoprice=sop2.find_all('p',class_="prd-des ft-body-3-1")
oppoprices=[]

for i in oppoprice:
    k=i.get_text()
    oppoprices.append(k)

opponame=sop2.find_all('div',class_="info-des")
opponames=[]

for i in opponame:
    k=i.p.get_text()
    opponames.append(k)
    
#print(opponames)
    
oppop=zip(opponames,oppoimgs,oppolinks,oppoprices)
#print(oppo)

def oppo(request):
    return render(request,"oppo.html",{'oppo':oppop})





