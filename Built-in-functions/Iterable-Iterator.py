from collections import Iterator, Iterable

'''
可以直接作用于for循环的对象统称为可迭代对象(Iterable)。
可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)。
所有的Iterable均可以通过内置函数iter()来转变为Iterator。
Iterator继承自Iterable，Iterator包含__iter()和next()方法，而Iteratble仅仅包含iter__()

内置函数iter()仅仅是调用了对象的__iter()方法，所以list对象内部一定存在方法iter__()
内置函数next()仅仅是调用了对象的__next()方法，所以list对象内部一定不存在方法next__()，但是Itrator中一定存在这个方法。
for循环内部事实上就是先调用iter()把Iterable变成Iterator在进行循环迭代的。
'''
l = [1, 2, 3]

print(isinstance(l, Iterable))  #True
print(isinstance(l, Iterator))  #False

l = iter(l)    #   same as l = l.__iter__()

print(isinstance(l, Iterable))  #True
print(isinstance(l, Iterator))  #True

#iterable需要包含有__iter()方法用来返回iterator，而iterator需要包含有next__()方法用来被循环

#当循环以后就殆尽了，再次使用调用时会引发StopIteration异常。
#我们可以通过copy把迭代器保存起来，可以下次使用，注意，不可以通过直接赋值

import copy

deep_copy = copy.deepcopy(l)