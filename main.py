from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello flask!'

if __name__ == '__main__':
    # app.run(host='127.0.0.1',port=80,debug=True)
    app.run()