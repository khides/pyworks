import time
import folium
import pandas as pd

def df_GPS():
    global latlst
    global lonlst
    latlst = []
    lonlst = []
    df = pd.read_csv('007.csv')
    for i in range(len(df)):
        if df.iloc[i]["Message"] == ' MANUAL' or df.iloc[i]["Message"] == ' HOLD' or df.iloc[i]["Message"] == ' LAND' or df.iloc[i]["Message"] == ' TAKEOFF':
            latlst.append(df.iloc[i]["Latitude"])
            lonlst.append(df.iloc[i]["Longitude"])
            
            
def map_GPS():
    global latlst
    global lonlst
    try:
        startlat = latlst[0]
        startlon = lonlst[0]
        endlat = latlst[-1]
        endlon = lonlst[-1]
        m=folium.Map(location=[startlat,startlon],zoom_start=20)
        folium.Marker([startlat,startlon],popup='Start',
                        icon=folium.Icon(color="blue", icon="flag")).add_to(m)
        folium.Marker([endlat,endlon],popup='Drone',
                        icon=folium.Icon(color="red", icon="plane")).add_to(m)        
        sq = [
            (latlst[i], lonlst[i])
            for i in range(len(latlst))
        ]
        folium.PolyLine(locations=sq).add_to(m)    
        m.save('log.html')
    except Exception as e:
        return
    
if __name__ == "__main__":
    while True:
        df_GPS()
        map_GPS()
        time.sleep(1)