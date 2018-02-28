import collections

#tupled的扩展  可命名元组

#创建一个普通tuple
t=(1,2)
#创建一个扩展tuple的类，Mytuple
Mytuple=collections.namedtuple('Mytuples',['x','y'])

tu=Mytuple(1,2) #相当于给原来的值赋了一个key
print(t)
print(tu)
print(tu.x,tu.y)
'''
输出：
(1, 2)
Mytuples(x=1, y=2)
2
'''