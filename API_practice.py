import requests
import json
import pprint


url='https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric'
urlKobe=url.format(city='Kobe,Jp',key='14cb50f66e972053ea313bf8ed70facd')

jsondata=requests.get(urlKobe).json()
pprint.pprint(jsondata)

print('都市名=',jsondata['name'])
print('気温=',jsondata['main']['temp'])
print('天気=',jsondata['weather'][0]['main'])
print('天気詳細=',jsondata['weather'][0]['description'])


url='https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric'
urlLondon=url.format(city='London,UK',key='14cb50f66e972053ea313bf8ed70facd')

jsondata=requests.get(urlLondon).json()
pprint.pprint(jsondata)

print('都市名=',jsondata['name'])
print('気温=',jsondata['main']['temp'])
print('天気=',jsondata['weather'][0]['main'])
print('天気詳細=',jsondata['weather'][0]['description'])



url='https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}&lang=ja&units=metric'
urlFunamachi=url.format(zipcode='160-0006,Jp',key='14cb50f66e972053ea313bf8ed70facd')

jsondata=requests.get(urlFunamachi).json()
pprint.pprint(jsondata)

print('都市名=',jsondata['name'])
print('気温=',jsondata['main']['temp'])
print('天気=',jsondata['weather'][0]['main'])
print('天気詳細=',jsondata['weather'][0]['description'])

#with open('Funamachi.json','w') as f:
#    f.write(jsondata)


url='https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric'
urlForecast=url.format(city='Tokyo,JP',key='14cb50f66e972053ea313bf8ed70facd')

jsondata=requests.get(urlForecast).json()
#pprint.pprint(jsondata)

from datetime import timedelta,timezone,datetime
tz=timezone(timedelta(hours=+9),'JST')

for i in range(len(jsondata['list'])):
    print('UTC時刻=',jsondata['list'][i]['dt_txt'])
    print('日本時刻=',str(datetime.fromtimestamp(jsondata['list'][i]['dt'],tz))[:-6])
    print('都市名=',jsondata['city']['name'])
    print('気温=',jsondata['list'][i]['main']['temp'])
    print('湿度=',jsondata['list'][i]['main']['humidity'])
    print('気圧=',jsondata['list'][i]['main']['pressure'])
    print('最高気温=',jsondata['list'][i]['main']['temp_max'])
    print('最低気温=',jsondata['list'][i]['main']['temp_min'])
    print('潮位=',jsondata['list'][i]['main']['sea_level'])
    print('天気=',jsondata['list'][i]['weather'][0]['main'])
    print('天気詳細=',jsondata['list'][i]['weather'][0]['description'])
    print()



time=[]
temp=[]
humidity=[]


for i in range(len(jsondata['list'])):
    time.append(str(datetime.fromtimestamp(jsondata['list'][i]['dt'],tz))[:-9])
    temp.append(float(jsondata['list'][i]['main']['temp']))

from matplotlib import pyplot as plt
import seaborn as sns

sns.set(font=['Meiryo','Yu Gothic','Hiragino Maru Gothic Pro'])


plt.figure(figsize=(15,8))
plt.plot(time,temp,label='五日間の気温')
plt.ylim(-10,40)
plt.legend()
plt.show()


import pandas as pd
import pprint
df=pd.DataFrame(columns=['気温'])
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[:-9]
    temp=dat['main']['temp']
    df.loc[jst]=temp

pprint.pprint(df)
df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.legend()
plt.show()