for i in range(1):
    print(i)
    
    
# print(200//500)




        startpos = await drone.Precise_location(10)
        dist = gps_distance(lat1=startpos[0], # 距離を計算
                            lon1=startpos[1],
                            lat2=lat_target1,
                            lon2=lon_target1)
        n = dist // 500
        latlst = []
        lonlst = []
        for i  in range(n): # 距離の分だけ内分点を追加
            lat_point = (startpos[0] + lat_target1)*(i + 1)/(n + 1)
            lon_point = (startpos[1] + lon_target1)*(i + 1)/(n + 1)
            latlst.append(lat_point)
            lonlst.append(lonlst)         
        