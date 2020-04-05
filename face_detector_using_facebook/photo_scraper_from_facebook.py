import http.cookiejar
import urllib.request
import bs4
import xlrd
import time
import xlwt
import requests
from xlutils.copy import copy
wb=xlrd.open_workbook('photos.xlsx')
sheet=wb.sheet_by_index(0)
r=sheet.nrows
rb=copy(wb)
sheet=rb.get_sheet(0)

cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

authentication_url="https://m.facebook.com/login.php"

payload={
    'email':'9877335446',
    'pass':'faceforus'
    }
data=urllib.parse.urlencode(payload).encode('utf-8')
req= urllib.request.Request(authentication_url,data)
resp=urllib.request.urlopen(req)
contents=resp.read()

name=input("Enter the Name of the Person you want to check")
fb_id=input("Enter The Fb id of person")

#url="https://mbasic.facebook.com/"+fb_id+"/photos"
url="https://mbasic.facebook.com/"+fb_id
data=requests.get(url,cookies=cj)
soup=bs4.BeautifulSoup(data.text,'html.parser')
for i in soup.find_all('a',href=True):
    if i.text.lower()=="photos":
        url="https://mbasic.facebook.com/"+i['href']
        break


time.sleep(1)
data=requests.get(url,cookies=cj)
soup=bs4.BeautifulSoup(data.text,'html.parser')
for i in soup.find_all('a',href=True):
    if i.text.lower()=="see all":
        url="https://mbasic.facebook.com"+i['href']
        break

time.sleep(1)
print("Wait few seconds, we are Downloading Images of "+name)
data=requests.get(url,cookies=cj)
soup=bs4.BeautifulSoup(data.text,'html.parser')
ph_urls=[]
index=0
for i in soup.find_all('a',href=True):
    if (i['href'][0:6]).lower()=="/photo":
        nurl="https://mbasic.facebook.com"+i['href']
        ph_urls.append(nurl)
        index=index+1
    if index>=6:
        break
photos=[]
for url in ph_urls:
    time.sleep(1)
    data=requests.get(url,cookies=cj)
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    for i in soup.find_all('a',href=True):
        if i.text.lower()=='view full size':
            nurl="https://mbasic.facebook.com"+i['href']
            photos.append(nurl)
            break
num=0
for photo in photos:
    time.sleep(1)
    data=requests.get(photo,cookies=cj)
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    for i in soup.find_all('meta'):
        time.sleep(1)
        urllib.request.urlretrieve(i['content'][6:],"images/"+name.split(" ")[0]+str(num)+".jpg")
        sheet.write(r,0,name)
        sheet.write(r,1,fb_id)
        sheet.write(r,2,name.split(" ")[0]+str(num)+".jpg")
        r=r+1
        print("Downloaded "+str(num))
    num=num+1
rb.save("photos.xlsx")
print("Photos Downloaded Sucessfully:)")
