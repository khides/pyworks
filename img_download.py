#すべてのimgタブの画僧ファイルurlを表示する
import time
import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path
import urllib

load_url='https://www.ymori.com/books/python2nen/test2.html'
html=requests.get(load_url)
soup=bs(html.content,'html.parser')
out_folder=Path('download2')
out_folder.mkdir(exist_ok=True)

for element in soup.find_all('img'):
    src=element.get('src')
    imgurl=urllib.parse.urljoin(load_url,src)
    imgdata=requests.get(imgurl)
    filename=imgurl.split('/')[-1]
    print(imgurl,filename)
    
    out_path=out_folder.joinpath(filename)
    with open(out_path,'wb') as f:
        f.write(imgdata.content)
    time.sleep(1)