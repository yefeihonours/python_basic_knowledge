'''
map（）函数
两个参数一个是函数名，另一个是列表或元组
'''

a = [0,1,2,3,4,5,6,7]
m1 = map(lambda x:x+3, a)

for var in m1:
    print(var, '', end = '')
#输出 3 4 5 6 7 8 9 10

b = [1, 2, 3]
c = [4, 5, 6]
m2 = map(lambda x,y:x+y, b, c)

for var in m2:
    print(var, '', end = '')
#输出 5 7 9
