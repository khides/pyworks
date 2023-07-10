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
with open("config.yaml", mode = "r") as f:
    conf1 = OmegaConf.load(f)

dict_conf = {"target1":"changed"}
conf2 = OmegaConf.create(dict_conf)
print(OmegaConf.to_yaml(conf2))
print(OmegaConf.to_yaml(conf1))
conf = OmegaConf.merge(conf1, conf2)
print(OmegaConf.to_yaml(conf))
# OmegaConf.save(conf,"config.yaml")