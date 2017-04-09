# coding:utf-8

from flask import render_template,request,redirect,url_for,flash
from app.weixin import identify_wechat, handle_wechat
from app.main import main
from .. import crud, weather_api

@main.route('/weixin',methods=['GET'])
def weixing():
	signature = request.args["signature"]
	timestamp = request.args["timestamp"]
	nonce = request.args["nonce"]
	echostr = request.args["echostr"]
	# temparr = []
	# token = "dearweather"
	# temparr = [token,timestamp,nonce]
	# temparr.sort()
	# newstr = "".join(temparr)
	# sha1str = hashlib.sha1(newstr.encode('utf-8'))
	# temp = sha1str.hexdigest()
	# if signature == temp:
	# 	return echostr
	# else:
	# 	return 'False'

	return identify_wechat(signature, timestamp, nonce, echostr)

@main.route('/weixin',methods=['POST'])
def weixinp():
	request_text = request.get_data()
	return handle_wechat(request_text)


@main.route('/',methods=['GET','POST'])
def index():
	"""response index page"""
	if request.method == 'POST':
		if request.form['button'] == 'Query':
			city_name = request.form['city_name']
			client_ip = request.remote_addr
			tp = weather_api.ThinkPage()
			weather = tp.get_weather_from_api(city_name)
			# crud.insert_history(weather)
			return render_template('index.html',display='query',info=weather)
	else:
		if request.args.get('button') == 'History':
			his_info = crud.read_history()
			return render_template('index.html',display='history',info=his_info)
		elif request.args.get('button') == 'Help':
			help_info = crud.read_help()
			return render_template('index.html',display='help',info=help_info)
		elif request.args.get('button') == 'Modify':
			return redirect(url_for('main.update'))
	return render_template('index.html',info='Welcome')


@main.route('/modify',methods=['GET','POST'])
def update():
	"""response update page"""
	if request.method == 'GET':
		return render_template('modify.html',info='')
	else:
		# weather = {}
		# weather['city_name'] = request.form['city_name']
		# weather['status'] = request.form['weather_status']
		# weather['tempreture'] = request.form['tempreture']
		# weather['tempreture_unit'] = request.form['tempreture_unit']
		# if request.form['button'] == 'Update':
		# 	if len(crud.read_weather(weather['city_name'])) > 0:
		# 		crud.update_weather(weather)
		# 		flash("Update successfully")
		# 	else:
		# 		flash("No data, Query first")
		# 	info = []
		# elif request.form['button'] == 'Back':
		# 	return redirect(url_for('index'))
		# elif request.form['button'] == 'DB':
		# 	info = crud.read_weather()
		return render_template('modify.html',info='info')