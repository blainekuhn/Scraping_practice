# pip install beautifulsoup4
# pip install requests
# pip install lxml

#all kinds of vehicle lists 'https://vpic.nhtsa.dot.gov/api/'
#Example query - https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json

from bs4 import BeautifulSoup
import requests, urllib3, os, json, certifi
from pprint import pprint
urls = []
datas = []
new_urls = []
new_list = []
soupa = ""
filename = ''

url = "https://volcanoes.usgs.gov/volcanoes/kilauea/multimedia_videos.html"

r  = requests.get(url)
data = r.text
soup = BeautifulSoup(r.text, 'html.parser')

links = ['https://volcanoes.usgs.gov'+a.get('href') for a in soup.find_all('a') if '/vsc/movies' in a.get('href') and not a.get('href') == None]

#def list_models():
#link = 'https://en.wikipedia.org/wiki/List_of_car_brands'
#r = requests.get(link)

def breakdown(links):
  global url
  for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a'):
      if 'mp4' in a.get('href'):
        print(a.findParents())
        url = "https://volcanoes.usgs.gov"+a.get('href')
        print(url)
 #       download(url)


def download(url):
  global filename
  https = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
  filename = url.split('/')
  filename = filename[len(filename)-1]
  file = https.request('GET', url, preload_content=False)
  with open(filename, 'wb') as out:
    while True:
      data = file.read(1000000) #1MB
      if not data:
        break
      out.write(data)
  file.release_conn()
  

    


#for link in links:
#	r = requests.get(link)
#	soup = BeautifulSoup(r.text, 'html.parser')
#	for a in soup.find_all('a'):
#		if 'mp4' in a.get('href'):
#			print(a)

			

    
#  for a in soup.find_all('a'):
#    b = a.get('href')
#    soupa = BeautifulSoup(b.text, 'html.parser')
#    print(b, soupa.get('href'))







def get_model(): #trying to pull data from json file exported from link below
  #came_from = 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json'
  with open('makers.json') as f:
    contents = json.load(f)
  results = contents['Results']
  for a in results:
    name = a['Mfr_CommonName']
    country = a['Country']
    if country == "United States (USA)":
      if name != None:
        if name not in new_list:
          new_list.append(name)
    new_list.sort()
      #pprint(name)
  

#get_model()




def hints():
  for link in soup.find_all('a'):
    if "json" in link.get('href'):
      urls.insert(len(urls), furl+link.get('href'))
      print(furl+link.get('href'))

      #https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json
  #this is two entries from a JSON output of Get All Makes
  a = {"Count":8374,"Message":"Response returned successfully","SearchCriteria":null,"Results":[{"Make_ID":440,"Make_Name":"Aston Martin"},{"Make_ID":441,"Make_Name":"Tesla"}]}
  a["Results"][0]['Mfr_CommonName']
  


def bs():
  for link in urls:
    link = 'https://www.ranker.com'+link
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a'):
       if "//www.ranker.com/review/" in a.get('href'):
         print(a.get('href'))
    #data.append(BeautifulSoup(requests.get(link).text, 'html.parser'))


def asdfas():
  for a in urls:
    print(a)
    r = requests.get('https://www.ranker.com'+a)
    #print(r.text)
    data = r.text
    soup = BeautifulSoup(r.text, 'html.parser')
  
