import copy

list_1=[0,1,2,3]
list_2=copy.copy(list_1)

list_2.append('end')

print(list_1)
print(list_2)
