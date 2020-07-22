import urllib.request
import requests
import dlib, cv2, os
import numpy as np
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from imutils import face_utils

def CreateFolder(directory):
    try :
        if not(os.path.isdir(directory)):
            os.makedirs(directory)  
    except OSError:
        print('Error : Creating directory. ' + directory )

class Parser():
    def __init__(self, keywords):
        self.keywords = keywords
    
    def Set(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.root_path = './images'

    def CreateDirectory(self):
        CreateFolder(self.root_path)
        for k in self.keywords:
            sub_path = self.root_path + '/' + k
            CreateFolder(sub_path)

    def Crawl(self):
        for k in self.keywords:
            sub_path = self.root_path + '/' + k
            base_url = 'https://pixabay.com/ko/images/search/' + k
            self.driver.get(base_url)
            html_source = self.driver.page_source
            soup = BeautifulSoup(html_source)
            page = soup.find('form',{'action':'.','method':'get'}).get_text().replace('/ ','')
            max_page = int(page)

            n = 1
            for p in range(1, max_page+1):
                base_url ='https://pixabay.com/ko/images/search/' + k + '/?pagi=' + str(p)
                self.driver.get(base_url)
                html_source = self.driver.page_source
                soup = BeautifulSoup(html_source)

                all_meta = soup.find_all('meta',{'itemprop':'contentUrl'})
                for m in all_meta:
                    url = m.get('content')
                    
                    file_name = str(n) + '.jpg'
                    file_path = sub_path + '/' + file_name
                    with open(file_path, 'wb') as f:
                        response = requests.get(url, stream=True)                

                        if not response.ok:
                            print(response)

                        for block in response.iter_content(1024):
                            if not block:
                                break
                            f.write(block)
                    n += 1 
        self.driver.close


if __name__=='__main__':
    keywords = ['개','강아지','dog']
    p = Parser(keywords)
    p.Set()
    p.CreateDirectory()
    p.Crawl()