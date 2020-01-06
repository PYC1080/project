import time

from selenium import webdriver

from bs4 import BeautifulSoup





comments = open("C:/Users/user/Desktop/study/python/crawling/Crawling data.txt", 'w' , encoding='utf-8' )

browser = 'C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(browser)

driver.get('http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=003&aid=0007731025&date=20170123&type=1&rankingSectionId=100&rankingSeq=1&m_view=1&m_url=%2Fcomment%2Fall.nhn%3FserviceId%3Dnews%26gno%3Dnews003%2C0007731025%26sort%3Dlikability')

time.sleep(3)

for i in range(0, 90):

      driver.find_element_by_css_selector(".u_cbox_btn_more").click()

      time.sleep(3)

      i +=1



html = driver.page_source

bs = BeautifulSoup(html, 'html.parser')

contents = bs.find_all("span", {"class" : "u_cbox_contents"})

for i in contents :

      comments.write(str(i) + '\n')

comments.close()



