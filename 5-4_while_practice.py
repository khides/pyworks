import random

n=random.randint(0,9)
print(n)


rand_num=0
while rand_num!=4:
    rand_num=random.randint(0,9)
    print(rand_num)


while True:
    rand_num=random.randint(0,9)
    print(rand_num)
    if rand_num!=4:
            continue
    else:
            break


