test_file=open('test.txt','w')
test_file.write('Hello!')
test_file.flush()
test_file.close()
test_file=open('test.txt','r')
read_str=test_file.readline()
test_file.close()
print(read_str)


test_file=open('test2.txt','w')
test_file.write('Hello!!\npython\n')
test_file.close()
test_file=open('test2.txt','r')
Line=test_file.readline()
print(Line)
test_file.close()

test_file=open('test2.txt','r')
Lines=test_file.readlines()
print(Lines)
print(Lines[0])
print(Lines[0].strip())
test_file.close()


data=['1,2,3\n','4,5,6\n','7,8,9\n']
test_file=open('test3.txt','w')
test_file.writelines(data)
test_file.close()


test_file=open('test3.txt','r')
for line in test_file:
    print(line.strip())
test_file.close()


list1='-'.join(['a','b','c'])
print(list1)


test_file=open('test3.txt','r')
for line in test_file:
    temp_list=line.strip().split(',')
    output_line='\t'.join(temp_list)
    print(output_line)
test_file.close()


with open('test2.txt','r') as test_file: 
###test3.txtファイルを変数名test_fileとして開いて以下の操作をして閉じる
    for line in test_file:
        print(line.strip())


