# coding:utf-8
from flask import Flask, g, request
import hashlib
import msg

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello,Flask'

def verification(request):
	print(request.args)


@app.route('/weixin',methods=['GET'])
def weixin():
	temparr = []
	token = "ichat"
	signature = request.args["signature"]
	timestamp = request.args["timestamp"]
	nonce = request.args["nonce"]
	echostr = request.args["echostr"]
	temparr = [token,timestamp,nonce]
	temparr.sort()
	newstr = "".join(temparr)
	sha1str = hashlib.sha1(newstr)
	temp = sha1str.hexdigest()
	if signature == temp:
		return echostr
	else:
		return 'False'
		
@app.route('/weixin',methods=['POST'])
def weixin_reply():
	# if verification(request):
		data = request.data
		weather_data = msg.rec(data)
		# print(self.weather_display.format(provider='心知天气'.rjust(10,' '),city_name=city_name.ljust(5,' '),\
		# 	weather_status=weather_data['results'][0]['now']['text'].ljust(4,' '),\
		# 	temp=weather_data['results'][0]['now']['temperature']))
		echostr = msg.reply(data,weather_data['results'][0]['now']['text'])
		return echostr
app.run(debug=True,host='127.0.0.1',port=80)