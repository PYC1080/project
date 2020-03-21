# capstone design - iise

> web crawler logs

## 03.20

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import openpyxl
from selenium import webdriver
from selenium.common import exceptions
import urllib.request
from urllib import parse
import pyperclip
import time

cd_path = "E:/download folder/chrome_driver/chromedriver.exe"
md_path = "C:/Users/pyc/Desktop/Work/study/iise/result/"

now_time = datetime.now()
def search_news(max_news, search_item, start_date, end_date):

    # 크롬 웹페이지 - 네이버 url입력
    s_date = start_date.replace(".","")
    e_date = end_date.replace(".","")

    search_url = "https://search.naver.com/search.naver?where=news&query=" \
          + search_item + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
          + start_date + "&de=" \
          + end_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" \
          + s_date + "to" \
          + e_date + "%2Ca%3Aall&mynews=1&refresh_start=0&related=0"

    driver = webdriver.Chrome(cd_path)
    driver.get(search_url)
    driver.implicitly_wait(5)

    #신문사 조건 입력
    news_option = driver.find_element_by_link_text("언론사")
    webdriver.ActionChains(driver).click(news_option).perform()

    no_j = driver.find_element_by_class_name("_ca_1025") # 중앙일보
    no_c = driver.find_element_by_class_name("_ca_1023") # 조선일보
    no_h = driver.find_element_by_class_name("_ca_1028") # 한겨례
    no_k = driver.find_element_by_class_name("_ca_1032") # 경향신문

    webdriver.ActionChains(driver).click(no_j).perform()
    webdriver.ActionChains(driver).click(no_c).perform()
    webdriver.ActionChains(driver).click(no_h).perform()
    webdriver.ActionChains(driver).click(no_k).perform()

    time.sleep(2)

    ok_btn = driver.find_element_by_class_name("tx")
    webdriver.ActionChains(driver).click(ok_btn)

    #기간 내 뉴스 갯수 파악
    finNo = driver.find_element_by_class_name




def main():
    search_item = input("검색어를 입력하세요 : ")
    start_date = input("검색 시작 날짜를 입력하세요(YYYY.MM.DD) : ")
    end_date = input("검색 종료 날짜를 입력하세요(YYYY.MM.DD) : ")
    max_news = input("검색할 뉴스의 갯수를 입력하세요 : ")


    search_news(max_news, search_item, start_date, end_date)

    #make_data

main()
```

## 03.21 - 오전

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import openpyxl
from selenium import webdriver
from selenium.common import exceptions
import urllib.request
from urllib import parse
import pyperclip
import time

cd_path = "E:/download folder/chrome_driver/chromedriver.exe"
md_path = "C:/Users/pyc/Desktop/Work/study/iise/result/"

now_time = datetime.now()

def search_news(driver,search_url,search_item, start_date, end_date):

    # 크롬 웹페이지 - 네이버 url입력
    driver.get(search_url)
    driver.implicitly_wait(5)

    #신문사 조건 입력
    news_option = driver.find_element_by_link_text("언론사")
    webdriver.ActionChains(driver).click(news_option).perform()

    no_j = driver.find_element_by_class_name("_ca_1025") # 중앙일보
    no_c = driver.find_element_by_class_name("_ca_1023") # 조선일보
    no_h = driver.find_element_by_class_name("_ca_1028") # 한겨례
    no_k = driver.find_element_by_class_name("_ca_1032") # 경향신문

    webdriver.ActionChains(driver).click(no_j).perform()
    webdriver.ActionChains(driver).click(no_c).perform()
    webdriver.ActionChains(driver).click(no_h).perform()
    webdriver.ActionChains(driver).click(no_k).perform()

    time.sleep(2)

    ok_btn = driver.find_element_by_class_name("tx")
    webdriver.ActionChains(driver).click(ok_btn)

def crawler(search_url,search_item):

    #기간 내 뉴스 갯수 파악
    req = requests.get(search_url)
    no_cont = req.content
    bs = BeautifulSoup(no_cont, "html.parser")
    findNo = bs.find("div",{"class":"title_desc all_my"})
    totalNo = str(findNo).split()[4].replace("건</span></div>","")
    print(totalNo)

def main():
    search_item = input("검색어를 입력하세요 : ")
    start_date = input("검색 시작 날짜를 입력하세요(YYYY.MM.DD) : ")
    end_date = input("검색 종료 날짜를 입력하세요(YYYY.MM.DD) : ")
    # max_news = input("검색할 뉴스의 갯수를 입력하세요 : ")

    driver = webdriver.Chrome(cd_path)
    s_date = start_date.replace(".","")
    e_date = end_date.replace(".","")
    search_url = "https://search.naver.com/search.naver?where=news&query=" \
                 + search_item + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
                 + start_date + "&de=" \
                 + end_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" \
                 + s_date + "to" \
                 + e_date + "%2Ca%3Aall&mynews=1&refresh_start=0&related=0"

    search_news(driver,search_url,search_item, start_date, end_date)

    crawler(search_url,search_item)

    #make_data

main()
```

