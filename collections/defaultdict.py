import collections

#默认字典defaultdict是对字典的类型的补充，他默认给字典的值设置了一个类型。

dic=collections.defaultdict(list) #默认字典的value，也可以是元组(tuple)或字典(dict)
#相当于dic={}
dic["k1"]=[]