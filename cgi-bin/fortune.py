#!/usr/bin/env python
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')
###windowsでUTF-8に対応するためのコード

import cgitb
cgitb.enable() ###プログラム事態にエラーがあるときにwebブラウザにエラーを表示する

html_body='''<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>今日の運勢</title>
    </head>
    <body>
        {month:d}月生まれのあなたの今日の運勢は{fortune:s}です
    </body>
</html>'''

import cgi
param_data=cgi.FieldStorage()
month=int(param_data.getvalue('month')) ###URLの？以降からサーバーにデータを送るためのコード

import datetime
today=datetime.date.today()

contents={}
contents['month']=month
contents['fortune']=['大吉','中吉','吉','小吉','末吉','凶','大凶'][today.day*month%7]

print('Content-Type: text/html')    ###ヘッダ　ステータスラインはpython内蔵のサーバが自動的に返す
print('')                           ###一行の改行
print(html_body.format(**contents))       ###ボディ ###formatは辞書型を引数にとるときは**を付ける
