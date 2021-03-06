import collections

'''
Counter是对字典类型的补充，用于追踪值的出现次数，具备字典的所有功能 + 自己的功能
'''

a='abababsbsbhh'

c=collections.Counter(a) #直接列出每个元素出现了几次，传入列表和元组也一样
print(c)
#输出：Counter({'b': 5, 'a': 3, 'h': 2, 's': 2})

#most_common 列出Counter内的前几个
print(c.most_common())
print(c.most_common(1))
print(c.most_common(3))

'''
输出：
[('b', 5), ('a', 3), ('h', 2), ('s', 2)]
[('b', 5)]
[('b', 5), ('a', 3), ('h', 2)]
'''

#update 相加
c=collections.Counter(a)
c1=collections.Counter(a)
c.update(c1)
print(c)
#输出：Counter({'b': 10, 'a': 6, 'h': 4, 's': 4})

#subtract 减
aa=collections.Counter("as")
bb=collections.Counter("htw")
aa.subtract(bb) #aa-bb
print(aa)
#输出：Counter({'a': 1, 's': 1, 'h': -1, 't': -1, 'w': -1})

#elements  返回包含所有元素集合的迭代器
for item in c.elements():
    print(item, ' ', end='')