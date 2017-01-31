import sae

# 使用flask应用程序代替
from main import app
# def app(environ, start_response):
# 	"""wsgi可调用对象"""
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return ['Hello, index wsgi!'] # 返回一个可迭代值

application = sae.create_wsgi_app(app)
