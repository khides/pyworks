cities = ['稚内','旭川','留萌','札幌','岩見沢','倶知安','網走','北見','紋別','根室','釧路','帯広','室蘭','浦河','函館','江差','青森','むつ','八戸','盛岡','宮古','大船渡','仙台','白石','秋田','横手','山形','米沢','酒田','新庄','福島','小名浜','若松','水戸','土浦','宇都宮','大田原','前橋','みなかみ','さいたま','熊谷','秩父','千葉','銚子','館山','東京','大島','八丈島','父島','横浜','小田原','新潟','長岡','高田','相川','富山','伏木','金沢','輪島','福井','敦賀','甲府','河口湖','長野','松本','飯田','岐阜','高山','静岡','網代','三島','浜松','名古屋','豊橋','津','尾鷲','大津','彦根','京都','舞鶴','大阪','神戸','豊岡','奈良','風屋','和歌山','潮岬','鳥取','米子','松江','浜田','西郷','岡山','津山','広島','庄原','下関','山口','柳井','萩','徳島','日和佐','高松','松山','新居浜','宇和島','高知','室戸岬','清水','福岡','八幡','飯塚','久留米','佐賀','伊万里','長崎','佐世保','厳原','福江','熊本','阿蘇乙姫','牛深','人吉','大分','中津','日田','佐伯','宮崎','延岡','都城','高千穂','鹿児島','鹿屋','種子島','名瀬','那覇','名護','久米島','南大東','宮古島','石垣島','与那国島']
acodes = ['1100', '1200', '1300', '1400', '1500', '1600', '1710', '1720', '1730', '1800', '1900', '2000', '2100', '2200', '2300', '2400', '3110', '3120', '3130', '3310', '3320', '3330', '3410', '3420', '3210', '3220', '3510', '3520', '3530', '3540', '3610', '3620', '3630', '4010', '4020', '4110', '4120', '4210', '4220', '4310', '4320', '4330', '4510', '4520', '4530', '4410', '4420', '4430', '4440', '4610', '4620', '5410', '5420', '5430', '5440', '5510', '5520', '5610', '5620', '5710', '5720', '4910', '4920', '4810', '4820', '4830', '5210', '5220', '5010', '5020', '5030', '5040', '5110', '5120', '5310', '5320', '6010', '6020', '6110', '6120', '6200', '6310', '6320', '6410', '6420', '6510', '6520', '6910', '6920', '6810', '6820', '6830', '6610', '6620', '6710', '6720', '8110', '8120', '8130', '8140', '7110', '7120', '7200', '7310', '7320', '7330', '7410', '7420', '7430', '8210', '8220', '8230', '8240', '8510', '8520', '8410', '8420', '8430', '8440', '8610', '8620', '8630', '8640', '8310', '8320', '8330', '8340', '8710', '8720', '8730', '8740', '8810', '8820', '8830', '1000', '9110', '9120', '9130', '9200', '9300', '9410', '9420']
pcodes = ['1a', '1a', '1a', '1b', '1b', '1b', '1c', '1c', '1c', '1c', '1c', '1c', '1d', '1d', '1d', '1d', '2', '2', '2', '3', '3', '3', '4', '4', '5', '5', '6', '6', '6', '6', '7', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '11', '12', '12', '12', '13', '13', '13', '13', '14', '14', '15', '15', '15', '15', '16', '16', '17', '17', '18', '18', '19', '19', '20', '20', '20', '21', '21', '22', '22', '22', '22', '23', '23', '24', '24', '25', '25', '26', '26', '27', '28', '28', '29', '29', '30', '30', '31', '31', '32', '32', '32', '33', '33', '34', '34', '35', '35', '35', '35', '36', '36', '37', '38', '38', '38', '39', '39', '39', '40', '40', '40', '40', '41', '41', '42', '42', '42', '42', '43', '43', '43', '43', '44', '44', '44', '44', '45', '45', '45', '45', '46', '46', '46', '46', '47', '47', '47', '47', '47', '47', '47']

c2ac={}
for i in range(len(cities)):
  c2ac[cities[i]]=acodes[i]

print(c2ac['さいたま'])

c2pc={}
for i in range(len(cities)):
  c2pc[cities[i]]=pcodes[i]

print(c2pc['父島'])

prefs = ['北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '北海道', '青森', '青森', '青森', '岩手', '岩手', '岩手', '宮城', '宮城', '秋田', '秋田', '山形', '山形', '山形', '山形', '福島', '福島', '福島', '茨城', '茨城', '栃木', '栃木', '群馬', '群馬', '埼玉', '埼玉', '埼玉', '千葉', '千葉', '千葉', '東京', '東京', '東京', '東京', '神奈川', '神奈川', '新潟', '新潟', '新潟', '新潟', '富山', '富山', '石川', '石川', '福井', '福井', '山梨', '山梨', '長野', '長野', '長野', '岐阜', '岐阜', '静岡', '静岡', '静岡', '静岡', '愛知', '愛知', '三重', '三重', '滋賀', '滋賀', '京都', '京都', '大阪', '兵庫', '兵庫', '奈良', '奈良', '和歌山', '和歌山', '鳥取', '鳥取', '島根', '島根', '島根', '岡山', '岡山', '広島', '広島', '山口', '山口', '山口', '山口', '徳島', '徳島', '香川', '愛媛', '愛媛', '愛媛', '高知', '高知', '高知', '福岡', '福岡', '福岡', '福岡', '佐賀', '佐賀', '長崎', '長崎', '長崎', '長崎', '熊本', '熊本', '熊本', '熊本', '大分', '大分', '大分', '大分', '宮崎', '宮崎', '宮崎', '宮崎', '鹿児島', '鹿児島', '鹿児島', '鹿児島', '沖縄', '沖縄', '沖縄', '沖縄', '沖縄', '沖縄', '沖縄']

p2c={}
for i in range(len(prefs)):
  p2c.setdefault(prefs[i],[]).append(cities[i])

p2c['青森']

def get_url_by_city(cn):
  acode=c2ac[cn]
  pcode=c2pc[cn]
  url='https://weather.yahoo.co.jp/weather/jp/{x:s}/{y:s}.html'.format(x=pcode,y=acode)
  return url

get_url_by_city('種子島')

import requests
from bs4 import BeautifulSoup

def get_yweather_by_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rs = soup.find(class_='forecastCity')
    rs = [i.strip() for i in rs.text.splitlines()]
    rs = [i for i in rs if i != ""]
    return rs


def print_weather_of_city(city):
  url=get_url_by_city(city)
  infolist=get_yweather_by_url(url)
  inf='今日({date})の{cityname}の天気は、{weather}です。最高気温は{maxtemp}、最低気温は{mintemp}です。'.format(
      date=infolist[0],cityname=city,weather=infolist[1],maxtemp=infolist[2],mintemp=infolist[3])

  return inf

print(print_weather_of_city('網走'))


##cities=['稚内','旭川','留萌','札幌','岩見沢','倶知安','網走','北見','紋別','根室']


maxdict={}
mindict={}
cur=0
for city in cities:
  url=get_url_by_city(city)
  infolist=get_yweather_by_url(url)
  maxtemp=infolist[2]
  mintemp=infolist[3]
  maxtemp=maxtemp[:maxtemp.find('℃')]
  mintemp=mintemp[:mintemp.find('℃')]
  maxdict[city]=int(maxtemp)
  mindict[city]=int(mintemp)
  if cur==0:
    date=infolist[0]
    cur=1

maxsorted=sorted(maxdict.items(),key=lambda x:x[1],reverse=True)
minsorted=sorted(mindict.items(),key=lambda x:x[1])


print(maxsorted)
print(minsorted)


maxlist=[]
for i in range(len(maxsorted)):
  for j in range(len(maxsorted[0])):
    maxlist.append(maxsorted[i][j])

minlist=[]
for i in range(len(minsorted)):
  for j in range(len(minsorted[0])):
    minlist.append(minsorted[i][j])


maxtop10='''最高気温トップ10 ({date})\n 
1 位  {} : {} 度 \n
2 位  {} : {} 度 \n
3 位  {} : {} 度 \n
4 位  {} : {} 度 \n
5 位  {} : {} 度 \n
6 位  {} : {} 度 \n
7 位  {} : {} 度 \n
8 位  {} : {} 度 \n
9 位  {} : {} 度 \n
10 位  {} : {} 度 \n'''.format(date=date,*maxlist)

print(maxtop10)

print()


mintop10='''最低気温トップ10 ({date})\n 
1 位  {} : {} 度 \n
2 位  {} : {} 度 \n
3 位  {} : {} 度 \n
4 位  {} : {} 度 \n
5 位  {} : {} 度 \n
6 位  {} : {} 度 \n
7 位  {} : {} 度 \n
8 位  {} : {} 度 \n
9 位  {} : {} 度 \n
10 位  {} : {} 度 \n'''.format(date=date,*minlist)

print(mintop10)