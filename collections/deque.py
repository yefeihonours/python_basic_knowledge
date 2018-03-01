#双向队列，两头都可以取可以插
#线程安全
import collections
q=collections.deque() #创建队列
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
print(q)    #输出deque([4, 1, 2, 3])

#单向队列，一个方向拿
#线程安全
import queue
q=queue.Queue(10) #创建队列，指定最多放10个数据
q.put(1)    #进
q.put(2)
q.put(3)
print(q.get())   #取
print(q.get())
'''
队列和栈的结构:
    队列：先进先出
    栈：弹夹，后加先出
'''