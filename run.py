# coding:utf-8
import os
import datetime
from flask import render_template,request,redirect,url_for,flash
import hashlib
import msg
from weather_query import ThinkPage as TP
# from weather_query import BaiduMap as BM
from init import app,db
from orm import Weather,History


@app.route('/',methods=['GET','POST'])
def index():
	"""response index page"""
	if request.method == 'POST':
		if request.form['button'] == 'Query':
			city_name = request.form['city_name']
			client_ip = request.remote_addr
			weather = query_weather(city_name,client_ip)
			return render_template('index.html',display='query',info=weather)
	else:
		if request.args.get('button') == 'History':
			his_info = show_history()
			return render_template('index.html',display='history',info=his_info)
		elif request.args.get('button') == 'Help':
			help_info = show_help()
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
			if len(read_weather(weather['city_name'])) > 0:
				update_weather(weather)
				flash("更新成功")
			else:
				flash("没有该城市数据，不能更新，请先查询")
			info = []
		elif request.form['button'] == '返回':
			return redirect(url_for('index'))
		elif request.form['button'] == '本地数据':
			info = read_weather()
		return render_template('modify.html',info=info)

def query_weather(city_name,client_ip):
	"""query weather from api"""
	tp = TP()
	weather_dict = tp.get_weather_from_api(city_name)
	# life_dict = tp.get_life_from_api(city_name)
	if weather_dict == None:
		return ['no infomation']
	else:
		query_datetime = datetime.datetime.utcnow()#.strftime('%Y-%m-%d %H:%M:%S')		
		weather = {}
		weather['status'] = weather_dict['results'][0]['now']['text']
		weather['tempreture'] = weather_dict['results'][0]['now']['temperature']
		weather['city_name'] = weather_dict['results'][0]['location']['name']
		weather['client_ip'] = client_ip
		weather['query_utc_datetime'] = query_datetime
		weather['tempreture_unit'] = 'C'
		weather['user_name'] = 'guest'
		save_to_db(weather) 
		return ["City : "+ weather['city_name'] , "Weather: "+ weather['status'] ,"Tempreture: " + weather['tempreture'] + "C"]

def save_to_db(weather):
	"""insert or update a record"""
	a_history = History(weather['city_name'],weather['status'],\
		weather['query_utc_datetime'],int(weather['tempreture']),\
		weather['tempreture_unit'],weather['client_ip'],weather['user_name'])
	db.session.add(a_history)
	if len(read_weather(weather['city_name'])) > 0:
		update_weather(weather)
	else:
		insert_weather(weather)

def read_weather(city_name=None):
	"""read weather table"""
	row = []
	if city_name != None:
		local_data = Weather.query.filter_by(city=city_name).all()
	else:
		local_data = Weather.query.all()
	for r in local_data:
		row.append('No.'+str(r.id)+' City: '+r.city+' Weather: '+r.weather_status+' Tempreture: '+str(r.tempreture)+''+r.tempreture_unit)
	return row

def update_weather(weather):
	"""update weather table"""
	w = Weather.query.filter_by(city=weather['city_name']).first()
	w.weather_status = weather['status']
	w.tempreture = weather['tempreture']
	w.tempreture_unit = weather['tempreture_unit']
	db.session.add(w)

def insert_weather(weather):
	"""insert record into weather table"""
	insert_a_record = Weather(weather['city_name'],weather['status'],int(weather['tempreture']),weather['tempreture_unit'])
	db.session.add(insert_a_record)

def show_history():
	"""get query history from database"""
	history = []
	history_query = History.query.all()
	for his in history_query:
		history.append([his.city,his.weather_status,his.query_utc_time,\
			str(his.tempreture),his.tempreture_unit,his.user_name,his.client_ip])
	return history

def show_help():
	"""show help infomation"""
	help_info = ['输入 城市名，可获取城市的天气;','单击 帮助 按钮，获取帮助文档;',\
	'单击 历史 按钮，获取查询历史;','单击 更正 按钮，可以进入更正页面修改本地数据库数据。']
	return help_info

@app.route('/weixin',methods=['GET'])
def weixin():
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
		
@app.route('/weixin',methods=['POST'])
def weixin_reply():
	# if verification(request):
		data = request.data
		content = msg.rec(data)
		echostr = msg.reply(data,content)
		return echostr


if __name__ == '__main__':
	db.create_all()
	# tp = TP() # tp变量放在这里，本地运行正常，push到heroku却发生服务器内部错误
	app.run()
