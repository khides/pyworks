###リスト型
list_tohoku=[5349,5478,5344,4644,4968,6259]

for val in enumerate(list_tohoku):
    print(val)

for val in enumerate(list_tohoku):
    print('index={} -> {}'.format(*val))



###辞書型
country_code={81:'Nippon',86:'China',39:'Italia'}

print(country_code.get(81,'somewhere'))
print(country_code.get(89,'somewhere'))
print(country_code)

print(country_code.setdefault(81,'somewhere'))
print(country_code.setdefault(89,'somewhere'))
print(country_code)

###応用〜世界の国と都市〜
world_city={}
world_city.setdefault('Nippon',[]).append('Tokyo')
print(world_city)
world_city.setdefault('America',[]).append('New York')
print(world_city)
world_city.setdefault('America',[]).append('Los Angels')
print(world_city)



###セット型
duplicate_list=[1,2,2,3,3,3]
from_list=set(duplicate_list)
print(from_list)
print(list(from_list))


north_zoo={'elephant','lion','tiger','penguin','flamingo'}
south_zoo={'penguin','lion','elephant','ostrich'}

print(north_zoo.intersection(south_zoo))
print(north_zoo.difference(south_zoo))
print(south_zoo.difference(north_zoo))