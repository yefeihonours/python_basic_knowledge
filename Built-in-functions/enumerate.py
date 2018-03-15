#如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：

list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print(i ,list1[i])

#利用enumerate()会更加直接和优美：

list2 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list2):
    print(index, item)

#enumerate还可以接收第二个参数，用于指定索引起始值，如：

list3 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list3, 1):
    print(index, item)

#如果要统计文件的行数，可以这样写：

#count = len(open(filepath, 'r').readlines())

#这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
#可以利用enumerate()：

count = 0
for index, line in enumerate(open(filepath,'r')):
    count += 1
print('共计行数：',count)