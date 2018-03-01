'''
filter（）函数
包括两个参数，分别是function和list。该函数根据function参数返回的结果是否为真来过滤list参数中的项，最后返回一个新列表
'''

a=[0,1,2,3,4,5,6,7,8,9]
b=filter(lambda x:x<5, a)

for var in b:
    print(var,' ',end='')
#输出 0  1  2  3  4

c=filter(None, a)
#如果filter参数值为None，就使用identity（）函数，list参数中所有为假的元素都将被删除
for var in c:
    print(var,' ',end='')