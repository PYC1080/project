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

1. 기사별 댓글 긁어 오는 작업 들어가지 못함
2. 검색 조건 입력 후 기사 갯수 긁어오는 작업 하지 못함

## 03.21 - 저녁

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

def search_news(driver,search_url):

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

    ok_btn = driver.find_element_by_css_selector("button.impact._submit_btn")
    webdriver.ActionChains(driver).click(ok_btn).perform()


def crawler(search_url,search_item,search_page):

    #기간 내 뉴스의 총 갯수 파악
    search_url2 = search_url.replace("0&refresh_start=0&related=0","1&refresh_start=0&related=0")
    req = requests.get(search_url2)
    no_cont = req.content
    bs = BeautifulSoup(no_cont, "html.parser")
    findNo = bs.find("div",{"class":"title_desc all_my"})
    totalNo = int(str(findNo).split()[4].replace("건</span></div>","").replace(",",""))
    print(totalNo)

    #뉴스 비율 구하기
    pageNo = 1
    pageMax = int(totalNo)
    pageMax2 = pageMax * (int(search_url)/1000)
    print(pageMax)
    print(pageMax2)



def main():

    # test-data
    search_item = "코로나"
    start_date = "2020.03.19"
    end_date = "2020.03.20"
    search_page = 20

    # 데이터 입력
    # search_item = input("검색어를 입력하세요 : ")
    # start_date = input("검색 시작 날짜를 입력하세요(YYYY.MM.DD) : ")
    # end_date = input("검색 종료 날짜를 입력하세요(YYYY.MM.DD) : ")
    # # max_news = input("검색할 뉴스의 비율(%)을 입력하세요 : ")

    driver = webdriver.Chrome(cd_path)
    s_date = start_date.replace(".","")
    e_date = end_date.replace(".","")
    search_url = "https://search.naver.com/search.naver?where=news&query=" \
                 + search_item + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
                 + start_date + "&de=" \
                 + end_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" \
                 + s_date + "to" \
                 + e_date + "%2Ca%3Aall&mynews=1&refresh_start=0&related=0"

    search_news(driver,search_url)

    crawler(search_url,search_item,search_page)

    #make_data

main()
```

### 1) 해결

```
1. 검색 조건을 입력해 뉴스의 갯수를 구하기
```

### 2) 해결 중

```
1. 받아온 뉴스 갯수가 int형으로 변하지 않는 문제 발생
2. 받아온 뉴스 링크가 검색 조건을 입력하기 전으로 되어있어 신문사 조건이 들어가지 않은 채 뉴스의 갯수를 파악하는 문제 발생
```

### 3) 앞으로 작업할 것

```
1. 해당 페이지 기사 링크 따오기
2. 해당 링크 들어가 기사 댓글 총 갯수 파악하기
3. 파악한 댓글 중 긁어올 댓글 갯수 산정하기
4. 산정한 댓글 크롤링
5. 크롤링한 댓글 파일 저장
```

## 03.22 오전

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
import math
import request


cd_path = "E:/download folder/chrome_driver/chromedriver.exe"
md_path = "C:/Users/pyc/Desktop/Work/study/iise/result/"

now_time = datetime.now()

def search_news(driver,search_url):

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

    ok_btn = driver.find_element_by_css_selector("button.impact._submit_btn")
    webdriver.ActionChains(driver).click(ok_btn).perform()


def crawler(search_url,search_item,search_page,driver):

    #기간 내 뉴스의 총 갯수 파악
    now_url = driver.page_source
    now_bs = BeautifulSoup(now_url, "html.parser")
    # print(now_bs)
    findNo =  now_bs.find('div', class_="title_desc all_my")
    totalNo = int(str(findNo).split()[4].replace("건</span></div>","").replace(",",""))
    # print(totalNo)

    # 검색할 뉴스 페이지 수 구하기
    pageNo = int(totalNo) * int(search_page) / 1000
    Max_page = math.floor(int(pageNo))
    last_page = math.floor(pageNo * 10) - (Max_page*10)
    now_page = 1

    # 기사 페이지
    # while now_page <= Max_page:
    #
    #     print(now_page)
    page_url = driver.page_source
    # print(page_url)
    page_bs = BeautifulSoup(page_url, "html.parser")
    # print(page_bs)
    # 해당 페이지에서 네이사 기사에 실린 기사에 해당하는 경우 파싱
    for i in  page_bs.select("._sp_each_url"):
        try:
            if i["href"].startswith("https://news.naver.com"):
                # print(i["href"])
                news_url = i["href"]
                news_url_tail = news_url.replace("https://news.naver.com/main/read.nhn?","")
                news_url_head =  "https://news.naver.com/main/read.nhn?"
                news_url_body =  "m_view=1&includeAllCount=true&"
                total_url = news_url_head + news_url_body + news_url_tail
                # print(total_url)
                driver.get(total_url)
                time.sleep(1)

                # 기사 내 댓글 총 갯수 파악
                repl_url = driver.page_source
                # print(repl_url)
                repl_bs = BeautifulSoup(repl_url,"html.parser")
                repl_find = repl_bs.find('a', class_="u_cbox_btn_title")
                repl_no = str(repl_find).replace("<a class=\"u_cbox_btn_title\" data-action=\"count#toggle\" href=\"#\"><h5 class=\"u_cbox_title\">전체 댓글</h5><span class=\"u_cbox_count\">","").replace("</span><span class=\"u_cbox_ico_arrow\"></span></a>","")
                print(repl_no)

                

        except:
            continue


def main():

    # test-data
    search_item = "코로나"
    start_date = "2020.03.19"
    end_date = "2020.03.20"
    search_page = 20

    # 데이터 입력
    # search_item = input("검색어를 입력하세요 : ")
    # start_date = input("검색 시작 날짜를 입력하세요(YYYY.MM.DD) : ")
    # end_date = input("검색 종료 날짜를 입력하세요(YYYY.MM.DD) : ")
    # # max_news = input("검색할 뉴스의 비율(%)을 입력하세요 : ")

    driver = webdriver.Chrome(cd_path)
    s_date = start_date.replace(".","")
    e_date = end_date.replace(".","")
    search_url = "https://search.naver.com/search.naver?where=news&query=" \
                 + search_item + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
                 + start_date + "&de=" \
                 + end_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" \
                 + s_date + "to" \
                 + e_date + "%2Ca%3Aall&mynews=1&refresh_start=0&related=0"

    search_news(driver,search_url)

    crawler(search_url,search_item,search_page,driver)

    #make_data

main()
```

### 1) 해결

```
1. 받아온 뉴스 갯수가 int형으로 변하지 않는 문제 해결
2. 받아온 뉴스 링크가 검색 조건을 입력하기 전으로 되어있어 신문사 조건이 들어가지 않은 채 뉴스의 갯수를 파악하는 문제 해결
3. 해당 페이지 기사 링크 따오기
4. 해당 링크 들어가 기사 댓글 총 갯수 파악하기
```

### 2) 해결 중

```
1
```

### 3) 앞으로 작업할 것

```
1. 파악한 댓글 중 긁어올 댓글 갯수 산정하기
2. 산정한 댓글 크롤링
3. 크롤링한 댓글 파일 저장
```

