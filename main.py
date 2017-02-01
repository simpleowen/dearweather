# coding:utf-8
from flask import Flask, g, request
import hashlib
import msg
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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
		content = msg.rec(data)
		echostr = msg.reply(data,content)
		return echostr

# app.run(debug=True,host='127.0.0.1',port=80)