# coding:utf-8
from flask import Flask, g, request
import hashlib
import msg

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello,Flask'

@app.route('/weixin',methods=['GET','POST'])
def weixin():
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
		data = request.data
		weather_data = msg.rec(data)
		# print(self.weather_display.format(provider='心知天气'.rjust(10,' '),city_name=city_name.ljust(5,' '),\
		# 	weather_status=weather_data['results'][0]['now']['text'].ljust(4,' '),\
		# 	temp=weather_data['results'][0]['now']['temperature']))
		echostr = msg.reply(data,weather_data['results'][0]['now']['text'])
		return echostr
