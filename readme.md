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
