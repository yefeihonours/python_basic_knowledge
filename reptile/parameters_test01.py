# -*- coding: UTF-8 -*-
from urllib import request
'''
 url不仅可以是一个字符串，例如:http://www.baidu.com。
 url也可以是一个Request对象，这就需要我们先定义一个Request对象，然后将这个Request对象作为urlopen的参数使用。
'''
if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    html = response.read()
    # urlopen()返回的对象，可以使用read()进行读取，同样也可以使用geturl()方法、info()方法、getcode()方法。
    #geturl()返回的是一个url的字符串；
    #info()返回的是一些meta标记的元信息，包括一些服务器的信息；
    #getcode()返回的是HTTP的状态码，如果返回200表示请求成功。
    html = html.decode("utf-8")
    print(html)