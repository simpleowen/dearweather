申请公众号

注册云平台

建立一个github仓库

克隆到本地





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


绑定微信公众号
