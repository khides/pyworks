
#zip圧縮する
import zipfile
with zipfile.ZipFile('./random.zip','w') as zp:
    zp.write('random.txt',arcname=None,compress_type=zipfile.ZIP_DEFLATED,compresslevel=None)

#zp=zipfile.ZipFile('./random.zip','w')
#zp.write('random.txt',arcname=None,compress_type=zipfile.ZIP_DEFLATED,compresslevel=None)
#zp.close()


#bzip圧縮する
with zipfile.ZipFile('./random.bzip','w') as zp:
    zp.write('random.txt',arcname=None,compress_type=zipfile.ZIP_BZIP2,compresslevel=None)

#LZMA圧縮する
with zipfile.ZipFile('./random.lzma','w') as zp:
    zp.write('random.txt',arcname=None,compress_type=zipfile.ZIP_LZMA,compresslevel=None)





###shutilを用いる
import shutil
shutil.make_archive('random_shutil','zip','random')
