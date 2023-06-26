
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By

# options =  Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(executable_path=os.getcwd() +"/chromedriver", options=options)
# driver.get('https://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()







driver = webdriver.Chrome()

#Google mapsを開く
url = 'https://www.google.co.jp/maps/'
driver.get(url)

#検索蘭にキーワードを記入
keys = input("検索キーワード：")

#データ入力
id =driver.find_element(By.ID, "searchboxinput")
id.send_keys(keys)

time.sleep(1)

#クリック
search_button = driver.find_element(By.XPATH,"//*[@id='searchbox-searchbutton']")
search_button.click()

time.sleep(3)

login_button = driver.find_element(By.CLASS_NAME,"")
login_button.click()

time.sleep(3)

#HTMLを解析
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

#取得したい要素を取得
title = soup.find(class_="GLOBAL__gm2-headline-5 section-hero-header-title-title")
link = soup.find_all(class_="section-info-text")

#出力
print("-------------------------------")
print(title.text.strip())
print(link[0].text.strip())
print(link[2].text.strip())
print(link[3].text.strip())
# print("-------------------------------")