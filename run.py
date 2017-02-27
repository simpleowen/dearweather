# coding:utf-8
import os
from flask import render_template,request,redirect,url_for,flash
import hashlib
import msg
from weather_query import ThinkPage as TP
# from weather_query import BaiduMap as BM
from init import app
# from orm import Weather,History
from orm import CRUD


@app.route('/',methods=['GET','POST'])
def index():
	"""response index page"""
	if request.method == 'POST':
		if request.form['button'] == 'Query':
			city_name = request.form['city_name']
			client_ip = request.remote_addr
			weather = tp.query_weather(city_name,client_ip)
			return render_template('index.html',display='query',info=weather)
	else:
		if request.args.get('button') == 'History':
			his_info = crud.show_history()
			return render_template('index.html',display='history',info=his_info)
		elif request.args.get('button') == 'Help':
			help_info = crud.show_help()
			return render_template('index.html',display='help',info=help_info)
		elif request.args.get('button') == 'Modify':
			return redirect(url_for('modify'))
	return render_template('index.html',info='')

@app.route('/modify',methods=['GET','POST'])
def modify():
	"""response update page"""
	if request.method == 'GET':
		return render_template('modify.html',info='')
	else:
		weather = {}
		weather['city_name'] = request.form['city_name']
		weather['status'] = request.form['weather_status']
		weather['tempreture'] = request.form['tempreture']
		weather['tempreture_unit'] = request.form['tempreture_unit']
		if request.form['button'] == '更正':
			if len(crud.read_weather(weather['city_name'])) > 0:
				crud.update_weather(weather)
				flash("更新成功")
			else:
				flash("没有该城市数据，不能更新，请先查询")
			info = []
		elif request.form['button'] == '返回':
			return redirect(url_for('index'))
		elif request.form['button'] == '本地数据':
			info = crud.read_weather()
		return render_template('modify.html',info=info)

@app.route('/weixin',methods=['GET'])
def weixin():
	if request.method == 'GET':
		temparr = []
		token = "dearweather"
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
	else:
		data = request.data
		content = msg.rec(data)
		echostr = msg.reply(data,content)
		return echostr


if __name__ == '__main__':
	crud = CRUD()
	tp = TP()
	app.run(debug=True)
