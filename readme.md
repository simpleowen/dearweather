申请公众号

注册云平台

建立一个github仓库

克隆到本地

http://www.sinacloud.com/doc/sae/tutorial/helloworld-for-linux-mac.html



flask MVP

> python main.py

PermissionError: [Errno 13] Permission denied

使用sudo提权

> sudo python main.py

ImportError: No module named flask

[System-Wide Installation](http://flask.pocoo.org/docs/0.10/installation/#system-wide-installation)

> sudo python main.py


部署到云平台，新浪

在本地的代码仓库里，添加一个新的git远程仓库 sae
> git remote add sae https://git.sinacloud.com/iyouchat

编辑代码并将代码部署到 `sae` 的版本1。
> git add .
> git commit -m 'Init my first app'
> git push sae master:1

提示输入用户名和密码


推送成功后，可在代码管理中看到已部署的代码版本

[代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git)


最后，你可以使用 [credential helper](https://git-scm.com/docs/gitcredentials) 来避免每次提交都要输入密码，如何配置可以参见：https://help.github.com/articles/caching-your-github-password-in-git/




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





绑定微信公众号
