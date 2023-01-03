with open('random.txt','w') as random_file:
    for i in range(250):
        random_file.write('AGCT')

with open('random.txt','r') as random_file:
    for line in random_file:
        print(line.strip())
    print('\n')
    print(random_file.readlines())


###random_file=open('random.txt','r')
#print(random_file.readlines())


with open('random2.txt','w') as f:
    for i in range(2500):
        f.write('AGCT')

import random
with open('random3.txt','w') as f:
    for i in range(10000):
        num=random.random()
        if num<0.25:
            f.write('A')
        elif 0.25<=num<0.5:
            f.write('G')
        elif 0.5<=num<0.75:
            f.write('C')
        elif 0.75<=num:
            f.write('T')
