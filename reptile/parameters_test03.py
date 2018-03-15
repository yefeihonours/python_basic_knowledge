# -*- coding: UTF-8 -*-
from urllib import request
'''
我们可以使用data参数，向服务器发送数据。根据HTTP规范，GET用于信息获取，POST是向服务器提交数据的一种请求，再换句话说：
从客户端向服务器提交数据使用POST；
从服务器获得数据到客户端使用GET(GET也可以提交，暂不考虑)。
如果没有设置urlopen()函数的data参数，HTTP请求采用GET方式，
也就是我们从服务器获取信息，如果我们设置data参数，HTTP请求采用POST方式，也就是我们向服务器传递数据。
data参数有自己的格式，它是一个基于application/x-www.form-urlencoded的格式，具体格式我们不用了解， 
因为我们可以使用urllib.parse.urlencode()函数将字符串自动转换成上面所说的格式。
本例向有道翻译发送data，得到翻译结果
'''
if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print("geturl打印信息：%s"%(response.geturl()))
    print('**********************************************')
    print("info打印信息：%s"%(response.info()))
    print('**********************************************')
    print("getcode打印信息：%s"%(response.getcode()))