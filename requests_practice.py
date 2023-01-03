from importlib.resources import path
import requests
from bs4 import BeautifulSoup as bs


#webページのhtmlテキストデータを入手する
load_url='https://www.ymori.com/books/python2nen/test2.html'
response=requests.get(load_url)
#print(type(response))
response.encoding=response.apparent_encoding
print(response.text)
#print(type(response.text))
#print(type(response.content))
#print(type(response.url))
#print(type(response.encoding))
#print(type(response.status_code))
#print(type(response.headers))
with open('download.txt','w') as f:
    f.write(response.text)
print()


#htmlテキストデータの一部を抽出する
soup=bs(response.content,'html.parser')
print(soup)

print(soup.find('title').text)#tag指定で最初のデータ
print(soup.find('h2').text)
print(soup.find('li').text)
print()
print(soup.find_all('title'))#tag指定ですべてのデータ
print(soup.find_all('h2'))
print(soup.find_all('li'))
print()
for value in soup.find_all('title'):
    print(value.text)
for value in soup.find_all('h2'):
    print(value.text)
for value in soup.find_all('li'):
    print(value.text)
print()
chap1=soup.find(id='chap1')#id指定
print(chap1)
print()
chap2=soup.find(id='chap2')
print(chap2)


#htmlのデータのうちurlを入手する
import urllib.parse
for element in soup.find_all('a'):
    print(element.text)
    url=element.get('href')
    urlabs=urllib.parse.urljoin(load_url,url)
    print(urlabs)


#webデータの画像データを読み込む
imgurl='https://www.ymori.com/books/python2nen/sample1.png'
imgdata=requests.get(imgurl)
filename=imgurl.split('/')[-1]
with open(filename,mode='wb') as f:
    f.write(imgdata.content)


#webデータの画像データをフォルダに読み込む
from pathlib import Path

out_folder=Path('download')
out_folder.mkdir(exist_ok=True)#downloadという名前のフォルダを作り\
                               #その情報を持った変数out_folderを作る
imgurl='https://www.ymori.com/books/python2nen/sample1.png'
imgdata=requests.get(imgurl)

filename=imgurl.split('/')[-1]
out_path=out_folder.joinpath(filename)#downloadフォルダの中に変数filenameで指定した\
                                      #ファイルを作り、その情報を持った変数out_pathを作る
with open(out_path,'wb') as f:
    f.write(imgdata.content)


