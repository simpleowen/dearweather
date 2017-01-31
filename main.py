# coding:utf-8
from flask import Flask, g, request
import hashlib

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
	return 'Hello,Flask'

@app.route('/weixin')
def verify_weixin():
	if request.method == 'GET':
		if len(request.args) > 3:
			temparr = []
			token = "ichat"
			signature = request.args["signature"]
			timestamp = request.args["timestamp"]
			nonce = request.args["nonce"]
			echostr = request.args["echostr"]
			temparr.append(token)
			temparr.append(timestamp)
			temparr.append(nonce)
			temparr.sort()
			newstr = "".join(temparr)
			sha1str = hashlib.sha1(newstr)
			temp = sha1str.hexdigest()
			if signature == temp:
				return echostr
			else:
				return "认证失败，不是微信服务器的请求！"
	else:
		return "你请求的方法是：" + request.method
