###リストを用いたfor文

list_tohoku=[5349,5478,5344,4644,4968,6259]
list_shikoku=[3148,2991,2966,2457]
for val in list_tohoku:
    print(val)  
    
avg_tohoku=0
for val in list_tohoku:
    avg_tohoku+=val
avg_tohoku/=len(list_tohoku)
print(avg_tohoku)


avg_tohoku2=0
for i in range(6):
    avg_tohoku2+=list_tohoku[i]
avg_tohoku2/=len(list_tohoku)
print(avg_tohoku2)

avg_shikoku=0
for val in list_shikoku:
    avg_shikoku+=val
avg_shikoku/=len(list_shikoku)
print(avg_shikoku)


###辞書型を用いたfor文
dict_tohoku={'aomori':5349,'akita':4644,'sendai':5344,'Yamagata':4968.0,\
    'fukushima':6259,'morioka':5478}

for val in dict_tohoku:
    print(val) ###valはキーのほうのみ

avg_tohoku=0
for val in dict_tohoku: ###キーはどの順で呼び出されるか分からない
    avg_tohoku+=dict_tohoku[val]
avg_tohoku/=len(dict_tohoku)
print(avg_tohoku)


