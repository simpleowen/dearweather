import MySQLdb
from flask import Flask, g, request

app = Flask(__name__)
app.debug = True

# from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
#     MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
# )

# @app.before_request
# def before_request():
#     g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
#                            MYSQL_DB, port=int(MYSQL_PORT))

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

@app.route('/')
def hello():
	s = GET()
    return s

# @app.route('/demo', methods=['GET', 'POST'])
# def greeting():
#     html = ''

#     if request.method == 'POST':
#         c = g.db.cursor()
#         c.execute("insert into demo(text) values(%s)", (request.form['text']))

#     html += """
#     <form action="" method="post">
#         <div><textarea cols="40" name="text"></textarea></div>
#         <div><input type="submit" /></div>
#     </form>
#     """
#     c = g.db.cursor()
#     c.execute('select * from demo')
#     msgs = list(c.fetchall())
#     msgs.reverse()
#     for row in msgs:
#         html +=  '<p>' + row[-1] + '</p>'

#     return html

import hashlib
# import web

def GET():
    try:
        data = request.get_data()
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "ichat" #请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception, Argument:
        return Argument
