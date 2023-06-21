import pandas as pd
import folium

m=folium.Map(location=[35.942957,136.198863],zoom_start=20)
m.save('sabae.html')



df=pd.read_csv('200.csv',encoding='shift-jis')
print(df.head())
print(df.columns.values)

hydrant=df[['緯度','経度']].values
print(hydrant)

for value in hydrant:
    folium.Marker([value[0],value[1]]).add_to(m)

m.save('hydrant.html')


m=folium.Map(location=[35.942957,136.198863],zoom_start=20)
folium.Circle(location=[35.942957,136.198863],\
    radius=100,color='red',fill=True).add_to(m)
df=pd.read_csv('898.csv')

print(df.columns.values)
store=df[['緯度','経度','店舗名(日本語)']].values
print(store)

for value in store:
    folium.Marker([value[0],value[1]],tooltip=value[2],\
        icon=folium.Icon(color='red',icon='home',icon_color='yellow')).add_to(m)
m.save('store.html')
