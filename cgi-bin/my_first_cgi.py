#!/usr/bin/env python
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')

import cgitb
cgitb.enable()

html_body='''<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>CGI</title>
    </head>
    <body>
        初めてのCGI
    </body>
</html>'''

print('Content-Type: text/html')    ###ヘッダ　ステータスラインはpython内蔵のサーバが自動的に返す

print('')                           ###一行の改行
print(html_body)                    ###ボディ