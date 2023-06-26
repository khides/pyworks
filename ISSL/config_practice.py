from omegaconf import OmegaConf
import sys

with open("config.yaml") as f:
    conf = OmegaConf.load(f)
    
print(conf.target1["latitude"])