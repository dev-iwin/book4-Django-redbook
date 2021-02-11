# 2.4.4 wsgiref.simple_server 모듈
# 예제 2-16 : WSGI 서버
# wsgi-server>notepad my_wsgiserver.py
''' 2.3.1 간단한 웹 서버 실습 방식과 비슷하지만
애플리케이션 로직을 작성하는 함수가 추가되었다 '''


from wsgiref.simple_server import make_server

def my_app(environ, start_response):

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    response = [b"This is a sample WSGI Application."]

    return response

if __name__ == '__main__':
    print("Started WSGI Server on port 8888...")
    server = make_server('', 8888, my_app)
    server.serve_forever()