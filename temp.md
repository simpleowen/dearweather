通过微信公众号查询城市天气



#申请公众号



#注册云平台

建立一个github仓库

克隆到本地

http://www.sinacloud.com/doc/sae/tutorial/helloworld-for-linux-mac.html



#flask MVP

> python main.py

PermissionError: [Errno 13] Permission denied

使用sudo提权

> sudo python main.py

ImportError: No module named flask

[System-Wide Installation](http://flask.pocoo.org/docs/0.10/installation/#system-wide-installation)

> sudo python main.py


#部署到云平台，新浪

在本地的代码仓库里，添加一个新的git远程仓库 sae
> git remote add sae https://git.sinacloud.com/iyouchat

编辑代码并将代码部署到 `sae` 的版本1。
> git add .
> git commit -m 'Init my first app'
> git push sae master:1

提示输入用户名和密码


推送成功后，可在代码管理中看到已部署的代码版本

[代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git)


IOError: Unable to open 'index.wsgi'


多次推送，部署时间不变，没有commit信息，没有操作者

添加index.html后再推送依然故障如旧


以版本2的方式推送

> git push sae master:2


这次有操作者和commit信息了，但链接依然打不开


google `IOError: Unable to open 'index.wsgi'`

说少了`index.wsgi`文件，建议看这两个官方链接


[新手入门](http://www.sinacloud.com/doc/sae/tutorial/index.html)

[python入门指南](http://www.sinacloud.com/doc/sae/python/tutorial.html)


再次push到版本1，

打开链接成功


还发现部署时间是不变的，而且没有操作者和commit信息。


所以可以删除2版本

> git push sae :2



每次都要输入用户名和密码，不方便

可以使用 [credential helper](https://git-scm.com/docs/gitcredentials) 来避免每次提交都要输入密码，如何配置可以参见：https://help.github.com/articles/caching-your-github-password-in-git/


#绑定微信公众号

填写配置信息后，

Token验证失败。

在[微信的入门指引](https://mp.weixin.qq.com/wiki)中有这样一句话，

> 3） 现在选择提交肯定是验证token失败，因为还需要完成代码逻辑

现在提交的文件中，有两个文件包含代码

index.wsgi

main.py


打开链接，返回的是'hello world'.

两串代码中都是return hello world，

为了确定是哪个代码在响应，修改其中一个返回值

将index.wsgi的返回值改为

return index.wsgi


再次提交到sae，打开链接返回‘index wsgi’

说明打开链接，index.wsgi负责响应。


flask的代码还没有起到作用


#所以这个index.wsgi的作用是什么？？？

WSGI是Web Server Gateway Interface的缩写

看sae帮助文档[参考](http://www.sinacloud.com/doc/sae/python/tutorial.html#shi-yong-web-kai-fa-kuang-jia)

index.wsgi是应用的代码入口文件

新浪云上的 Python 应用的入口为 index.wsgi:application ，也就是 index.wsgi 这个文件中名为 application 的 callable object。在 helloworld 应用中，该 application 为一个 wsgi callable object。

可调用对象是什么？

[wsgi理解](http://www.cnblogs.com/eric-nirnava/p/wsgi.html)

[WSGI](http://www.jianshu.com/p/34ee01d85b0a)

[WSGI简介](https://segmentfault.com/a/1190000003069785)

[PEP 3333 -- Python Web Server Gateway Interface v1.0.1](https://www.python.org/dev/peps/pep-3333/)

头晕，flask跟wsgi，跟web服务器，跟中间件啥关系？


在[WSGI简介](https://segmentfault.com/a/1190000003069785)中有这么一句，
Application端的实现一般是由Python的各种框架来实现的，比如Django, web.py等，一般开发者不需要关心WSGI的实现，框架会会提供接口让开发者获取HTTP请求的内容以及发送HTTP响应。

大概看了这么些链接后

这下放心了，可以专心搞flask

回头在看[新浪云sae入门指南](http://www.sinacloud.com/doc/sae/python/tutorial.html#shi-yong-web-kai-fa-kuang-jia)


可以稍微理解一些了

里面有[flask的实现](http://www.sinacloud.com/doc/sae/python/tutorial.html#flask)


File "/data1/www/htdocs/636/iyouchat/1/index.wsgi", line 3
SyntaxError: Non-ASCII character '\xe4' in file /data1/www/htdocs/636/iyouchat/1/index.wsgi on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details


源码文件头部添加`#coding:utf-8`

返回成功

> hello,flask


此时再次提交公众号服务器配置信息，依然提示token验证失败。

还有代码逻辑未完成？？？

继续看[微信开发入门指引](https://mp.weixin.qq.com/wiki)

将[新浪云sae入门指南](http://www.sinacloud.com/doc/sae/python/tutorial.html#shi-yong-web-kai-fa-kuang-jia)中的flask代码复制到main.py中提交后，打开链接异常


```
Traceback (most recent call last):
  File "/usr/local/sae/python/lib/python2.7/site-packages/sae/__init__.py", line 18, in new_app
    return app(environ, start_response)
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1306, in __call__
    return self.wsgi_app(environ, start_response)
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1294, in wsgi_app
    response = self.make_response(self.handle_exception(e))
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1062, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1058, in full_dispatch_request
    rv = self.preprocess_request()
  File "/usr/local/sae/python/lib/python2.7/site-packages/flask/app.py", line 1168, in preprocess_request
    rv = func()
  File "/data1/www/htdocs/636/iyouchat/1/main.py", line 14, in before_request
    MYSQL_DB, port=int(MYSQL_PORT))
  File "/usr/local/sae/python/lib/python2.7/site-packages/MySQLdb/__init__.py", line 81, in Connect
    return Connection(*args, **kwargs)
  File "/usr/local/sae/python/lib/python2.7/site-packages/MySQLdb/connections.py", line 187, in __init__
    super(Connection, self).__init__(*args, **kwargs2)
OperationalError: (1045, 'access deny')

```

最后一行是'access deny'，上边有MySQLdb的字样，且复制的代码中有导入MySQLdb

所以判断为sae上还没有创建数据库导致。

创建数据库实例，创建数据库，创建用户，建立demo表后，依然报同样的异常。

先注释掉main.py中的有关数据库的语句

继续看[微信开发入门指引](https://mp.weixin.qq.com/wiki)

在示例中，新增了一个处理文件handle.py

看逻辑流程，这个文件就是在验证token

所以我的应用中也需要增加验证token的代码


仿照[微信开发入门指引](https://mp.weixin.qq.com/wiki)的handle代码，为main.py增加token验证代码

web.py

import web
data = web.input()


flask里边用什么来获取

request.args


验证成功


#接收消息

URL接口验证以后，公众平台账号收到的消息将由微信服务器使用HTTP POST推送至该URL。消息内容为XML格式

解析xml

#返回数据



# 为sae添加第三方包依赖

在使用requests进行天气数据查询时，本地环境下正常，

但将源码上传到sae后，提示'no module named requests'，

原来第三方包需要安装到程序目录中一起上传到sae。

[添加第三方包依赖](http://www.sinacloud.com/doc/sae/python/tools.html#tian-jia-di-san-fang-yi-lai-bao)



# 接口调试

1. 微信提供了[在线接口调试功能](http://mp.weixin.qq.com/debug)
2. postman也是一款比较好的GET/POST调试工具
3. 可以在本地运行应用程序，在程序中嵌入print语句来进行调试



# 大坑-该公众号暂时无法提供服务，请稍后再试

在以下两种情况下都能正常返回数据，但是在微信公众号下面发信息却返回“该公众号暂时无法提供服务，请稍后再试”。

- 使用postman发送POST请求能正常返回天气数据

- [在线接口调试工具](http://mp.weixin.qq.com/debug)也能正确返回天气数据

看[微信开发文档](https://mp.weixin.qq.com/wiki)有下面的描述，

一旦遇到以下情况，微信都会在公众号会话中，向用户下发系统提示“该公众号暂时无法提供服务，请稍后再试”：

1、开发者在5秒内未回复任何内容

2、开发者回复了异常数据，比如JSON数据等

很快可以排除第一种情况，因为系统提示“该公众号暂时无法提供服务，请稍后再试”的时间在1秒左右。

那原因应该是开发者回复了异常数据。

为了排查这个异常数据的问题，检查回复消息函数，分别做了以下修改：

调整xml字符串的位置，确定不是换行或缩进的问题

用utf-8编码返回的中文字符串，但使用英文文本返回，问题依旧，确定不是编码的问题

最后发现是发送用户(FromUserName)和回复用户(ToUserName)位置没有调换造成。

发送消息与回复消息中的用户是要调换位置的，

发送消息中的发送用户是回复消息中的回复用户，

发送消息中的回复用户是回复消息中的发送用户。


# 解码问题

有时在源码文件中使用中文字符会出现以下异常：

> UnicodeDecodeError: 'ascii' codec can't decode byte 0xef in position 0: ordinal not in range(128)

解决这个问题有两个方法：

1.在源码文件中加入以下语句

> import sys  
> reload(sys)   
> sys.setdefaultencoding("utf-8")  

2.用utf-8解码中文字符串

> "广州".decode('utf-8')