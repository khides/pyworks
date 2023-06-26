import csv
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import bs4
from bs4 import BeautifulSoup
import requests
import numpy as np


area = '東京' # 店名のみだと絞り込めない場合があるため（住所などを用いてもいい）
filename = 'example.csv'
shop_index = 0 # 店名がある列を指定

def get_info(place_name):
    # 4. SeleniumでGoogle Mapsを開き、店名をキーにして検索
    key = place_name + "%20" + area
    url = 'https://www.google.co.jp/maps/search/' + key
    driver.get(url)
    time.sleep(3) # 検索結果の画面に遷移する間待つ

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # クラス名でそれぞれの情報を取得しているが、今後変更される可能性あり
    category = ''
    if soup.find(class_="DkEaL u6ijk") is not None:
        category = soup.find(class_="DkEaL u6ijk").text

    rating = ''
    if soup.find(class_="F7nice mmu3tf") is not None:
        rating = soup.find(
            class_="F7nice mmu3tf").contents[0].contents[0].contents[0].text

    return [rating, '【%s_%s】%s' % (rating, category, place_name), driver.current_url, category]


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# 2. CSVデータの読み込み
original_data = []
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        # 必要に応じて行を整形する
        # while len(row) != 7:
        #     row.pop(3)

        original_data.append(row)

# 3. 読み込んだCSVの各データの長さが同一かを確認する
iterator = iter(original_data)
first_row_length = len(next(iterator))
if not all(len(row) == first_row_length for row in iterator):
    raise ValueError('Not all lists have same length!')

result = []
for row in original_data:
    shop = row[shop_index]
    result.append(get_info(shop) + row)
    print(shop)

np_result = np.array(result)
sorted_result = np_result[np.argsort(np_result[:, 0])[::-1]] # Google Mapsの評価の高い順に並べ替え

# 5. 検索結果の情報を取得し、結果のCSVとして保存
result_filename = 'result_' + filename
with open(result_filename, 'w', encoding='utf_8_sig') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(sorted_result)
