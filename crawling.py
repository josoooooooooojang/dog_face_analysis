from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from bs4 import BeautifulSoup
import requests
import os

def CreateFolder(directory):
    try :
        if not(os.path.isdir(directory)):
            os.makedirs(directory)  
            # os.makedirs(os.path.join(directory))            
    except OSError:
        print('Error : Creating directory. ' + directory )

# Set Keyword to save
keywords = ['개','강아지','dog']

# Create root directory
rootPath = './images'
CreateFolder(rootPath)

# Set 'driver.exe' (need to absoulte path)
driver = webdriver.Chrome("C:\\Users\\조수장\\Desktop\\project\\look_like_dog\\chromedriver.exe")

for k in keywords:
    subPath = rootPath+'/'+k
    CreateFolder(subPath)
    driver.get('https://pixabay.com/ko/images/search/'+k)
    html = driver.page_source
    soup = BeautifulSoup(html)
    pagi = soup.find('form',{'action':'.','method':'get'}).get_text().replace('/ ','')
    allPage = int(pagi)

    n = 1
    for p in range(1,allPage+1):
        url ='https://pixabay.com/ko/images/search/'+k+'/?pagi='+str(p)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html)

        objects = soup.find_all('meta',{'itemprop':'contentUrl'})
        for o in objects:
            link = o.get('content')
            with open(subPath+'/'+str(n)+'.jpg', 'wb') as handle:
                response = requests.get(link,stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)   
            n += 1

driver.close
