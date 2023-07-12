from omegaconf import OmegaConf
import sys
# condition =""
# try:
#     condition = sys.argv[1]
# except IndexError as e:
#     print(e)

# # condition = sys.argv[1]
# if condition == "a":
#     with open("config.yaml") as f:
#         conf = OmegaConf.load(f)
#     print(conf.target1["latitude"])
# else :
#     print("not initialized")


# if __name__ == "__main__":
#     lst = ["a","b","c"]
    
#     x = str(input())
#     if  x in lst:
#         print(1)
#         exit()
#     print(2)    

from tqdm import tqdm
import time
from itertools import count

latitudelst = [1,0,1,2,3,4,5,6,7,8,9,10]
longitudelst = [0,1,1,2,3,4,5,6,7,8,9,10]

with open("config.yaml", mode = "r") as f:
    conf1 = OmegaConf.load(f)
print("\n現在のconfig file: \n")
print(OmegaConf.to_yaml(conf1))


while True:
    flag = int(input("start: 1, finish: 0  "))
    if flag == 0 or flag == 1:
        break
    print("Error :input 0 or 1")

if not flag:
    print("-- finish program")
    exit()

while flag:
    iter_cnt1 = count(0)
    iter_cnt2 = count(0)
    counter = 0
    latlst = []
    lonlst = []
    # print(f"\nnum_satellites:{drone.num_satellites}")
    print("-- get position start")
    pbar = tqdm(total=10)
    while counter < 11:
        time.sleep(1)
        latitude = latitudelst[next(iter_cnt1)]
        longitude = longitudelst[next(iter_cnt2)]
        if latitude == 0.0 and longitude == 0.0:
            continue
        latlst.append(latitude)
        lonlst.append(longitude)            
        pbar.update()
        counter += 1
    pbar.close()

    lat = sum(latlst)/len(latlst)
    lon = sum(lonlst)/len(lonlst)
    print(latlst, lonlst)
    posdict = {"latitude": lat, "longitude": lon}    
    print(f"\n-- position is {posdict}")
    while True:
        flag = int(input("try again: 1 , save: 0  "))
        if flag == 0 or flag == 1:
            break
        print("Error: input 0 or 1")
        
target = input("読み込んだセットポイントのラベルを決めてください")
dict_conf = {target:posdict}
conf2 = OmegaConf.create(dict_conf)
print("\nconfig fileの変更点: ")
print(OmegaConf.to_yaml(conf2))
        

print("現在のconfig file: ")
print(OmegaConf.to_yaml(conf1))


while True:    
    mergeflag = input("変更をmergeしますか？ [yes/no]")
    if mergeflag == "yes":
        conf = OmegaConf.merge(conf1, conf2)
        print(OmegaConf.to_yaml(conf))
        OmegaConf.save(conf,"config.yaml")
        exit()
    elif mergeflag == "no" :
        print("変更を破棄します")
        exit()
    else :
        print("Error: input yes or no")
        
