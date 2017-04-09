# 功能描述

通过微信公众号查询城市天气

# 公众号

![公众号](http://7xrtxq.com1.z0.glb.clouddn.com/qrcode_for_gh_516eed9b8a4f_430.jpg)


# 操作

1. 添加公众号

1. 输入城市名

![查询城市天气](https://cloud.githubusercontent.com/assets/17614465/22534929/7f681b9e-e932-11e6-86b5-4e651df32fa9.png)


# 文件说明

文档结构：

```
.
├── init
│   ├── __init__.py
│   ├── templates
│   │   ├── index.html
│   │   └── modify.html
│   └── weather.db
├── orm.py
├── Procfile
├── readme.md
├── requirements.txt
├── run.py
├── runtime.txt
└── weather_query.py

```

init：包

__init__.py：初始化应用程序实例和数据库

weather.db ： 数据库

templates ： 模板目录

templates/index.html : 主页模板

templates/modify.html :更正模板

orm.py：对象关系模型，关联数据库中的表

Procfile：heroku部署必须文件

requirements.txt：heroku部署必须文件

run.py : 主程序

runtime.txt：指定heroku端python版本

weather_query.py ： 心知天气接口



# 依赖

flask

requests

flask-sqlalchemy

flask-moments


# 运行

> python run.py


# 功能

- [x] 查询实时天气
- [x] 保存API数据到本地数据库
- [x] 更正本地数据库中的天气数据
- [ ] 用户登陆
- [ ] 定时爬取API数据
- [x] 本地时间交给浏览器渲染 ~~根据时区显示本地时间~~
- [x] 消息闪现
- [ ] 前端框架
