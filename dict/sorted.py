'''
sorted(iterable,key,reverse)

其中iterable表示可以迭代的对象，例如可以是dict.items()、dict.keys()等;
key是一个函数，用来选取参与比较的元素，reverse则是用来指定排序是倒序还是顺序
'''

dic = {'xiaoming':1, 'zhangsan':3, 'wangwu':2}

s1 = sorted(dic.keys(), reverse = True)  #按照key排序,reverse=true是倒序，reverse=false时则是顺序，默认时reverse=false

print(s1)    #输出['wangwu', 'xiaoming', 'zhangsan']

s2 = sorted(dic.items(), key = lambda item:item[1]) #按照value排序

print(s2)   #输出[('xiaoming', 1), ('wangwu', 2), ('zhangsan', 3)]
