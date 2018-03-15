####字典的定义 key: value
info ={
    'stu1001':"TengLan Wu",
    'Stu1002':"Longze Loula",
    'stu1103':"XiaoZe Maliya",
}
#####查询 字典的数据###############
#####查询所有，但是字典是无序的
print(info)

#如果查询一个只需要查询对方的key
print(info["stu1001"])

#不报错方式查询（安全点）
print(info.get("stu1001"))



####### 修改######

info["stu1001"]="武藤兰"
print(info)

#########添加#########
info["stu1004"]="CangjingKong"
print(info)

########删除######## 两种方法
#第一种
#del info["stu1001"]
print(info)

#第二种
info.pop("stu1103")
print(info)

#还有一个随机删除
info.popitem()

#判断字典里面存不存在这个key

print('stu1005' in info ) # 有的话返回TRUE

#查询所有的values
print(info.values())

#查询所有的key
print(info.keys())

b={
    'stu1001':"liang",
    1:2,
    2:5
}
#update 合并字典
info.update(b)
print(info)

#items #字典转为列表
print(info.items())

#初始化一个新的字典
#c=info.fromkeys([6,7,8])
c=dict.fromkeys([7,8,9],"test")
print(c)

#fromkeys 坑的地方
#如果里面嵌套了一个字典，修改一个的时候就会修改所有的
#就像浅层copy一样的
d=dict.fromkeys([7,8,9],[1,{"name":"liang"},444])
d[7][1]['name']="cc"
print(d)

#最基本的循环
for i in info:
    print(i,info[i])

#这种循环花的时间比第一种长，建议使用第一种循环
for k,v in info.items():

    print(k,v)