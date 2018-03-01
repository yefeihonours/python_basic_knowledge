from functools import reduce

'''
reduce（）函数
按照给定的方法把输入参数中上序列缩减为单个的值，具体的做法如下：
首先从序列中去除头两个元素并把它传递到那个二元函数中去，求出一个值，再把这个加到序列中循环求下一个值，直到最后一个值 。
'''

answer1 = reduce(lambda x,y:x*y, [1,2,3,4,5])
#((((1*2)*3)*4)*5

print('answer1 =',answer1)

answer2 = reduce(lambda x,y:x*y, [1,2,3], 10)
#((1*2)*3)*10

print('answer2 =',answer2)