###zipfile解凍

import zipfile
with zipfile.ZipFile('./random.zip','r') as zp:
    zp.extractall(path=None,members=None,pwd=None)
###path='./指定ディレクトリ/'
###members='['展開するファイル名',...]
###pwd
print(zp.namelist())

with zipfile.ZipFile('./random.zip','r') as zp:
    with zp.open('random.txt') as file:
        print(file.read())

print('\n')

with zipfile.ZipFile('./random.zip','r') as zp:
    print(zp.read('random.txt'))

#zp=zipfile.ZipFile('./random.zip','r')
#zp.extractall()
#zp.close()



###shutil解凍
import shutil
shutil.unpack_archive('random_shutil.zip','random_shutil_unzip')




###zipeile...
# ファイルごとの圧縮解凍ができ、また細かい設定、文字化け対策ができる
# フォルダを一気に圧縮できない(コードが増え、ミスが増える)

###shutil...
# フォルダごとに一気に圧縮、解凍ができる
# ファイルごとに詳細設定ができない