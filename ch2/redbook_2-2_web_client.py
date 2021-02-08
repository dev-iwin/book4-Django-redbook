# # 2.2 웹 클라이언트 라이브러리 (챕터2의 2.)
#
# # 2.2.1 urllib.parse 모듈
# from urllib.parse import urlparse
# result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
# print(result)
#
# # 2.2.2 urllib.request module
# # 예제 2-1 : urlopen() 함수 - GET 방식 요청
# from urllib.request import urlopen
# f = urlopen("http://example.com")
# print(f.read(500).decode('utf-8'))
#
# '''
# HTTP GET 방식을 디폴트로 사용하여 웹 서버에 요청한 프로그램.
# 웹 브라우저와 다르게, html 형식의 데이터를 해석하지 않고 그대로 보여줌.
# <!doctype html>부터, html태그, head태그, body태그 전부.
#
# 위와 같은 명령을 쉘 프롬프트에서는 이렇게 하면 바로 실행 가능.
# >python -c "import urllib.request print(urllib.request.urlopen('http://www.example.com').read(500).decode('utf-8))"
#
# 2.2.2 urlopen() 함수 - POST 방식 요청 예제는 장고 프로젝트를 생성한 후 그 서버에서 진행 예정 (종종 그렇게 될 예정)
# '''
#
# # 예제 2-2 : urlopen() 함수 - POST 방식 요청
# # >python
# from urllib.request import urlopen
# data = "language=python&framework=django"
# f = urlopen(" http://127.0.0.1:8000/", bytes(data, encoding='utf-8'))
# print(f.read(500).decode('utf-8'))
#
#
# # 예제 2-3 : ulropen()함수 - Request 클래스로 요청 헤더 지정
# # Request 객체를 생성한 뒤, add_header() 메서드 추가해서 웹서버에 요청보내기
# # >python
# from urllib.request import urlopen, Request
# from urllib.parse import urlencode
# data = "language=python&framework=django"
# f = urlopen(" http://127.0.0.1:8000/", bytes(data, encoding='utf-8'))
# print(f.read(500).decode('utf-8'))
#
# url = 'http://127.0.0.1:8000/'
# data = {
#     'name': '김석훈',
#     'email': 'shkim@naver.com',
#     'url': 'http://www.naver.com'
# }
# encData = urlencode(data)
# postData = bytes(encData, encoding='utf-8')
# req = Request(url, data=postData)
# req.add_header('Content-Type', 'application/x-www-form-urlencoded')
# f = urlopen(req)
# print(f.info())
# print(f.read(500).decode('utf-8'))
#
# # 예제 2-4 : urlopen()함수 - HTTPBasicAuthHandler 클래스로 인증 요청
# # >python
# from urllib.request import HTTPBasicAuthHandler, build_opener
# auth_handler = HTTPBasicAuthHandler()
# auth_handler.add_password(realm='ksh', user='shkim', passwd='shkimadmin', uri='http://127.0.0.1:8000/auth/')
# opener = build_opener(auth_handler)
# resp = opener.open('http://127.0.0.1:8000/auth/')
# print(resp.read().decode('utf-8'))
#
# # 예제 2-5 : urlopen() 함수 - HTTPCookieProcessor 클래스로 데이터를 포함하여 요청
# # >python
# from urllib.request import Request, HTTPCookieProcessor, build_opener
#
# url = 'http://127.0.0.1:8000/cookie/'
#
# # first request (GET) with cookie handler
# # 쿠키 핸들러 생성, 쿠키 데이터 저장은 디폴트로 CookieJar 객체를 사용함
# cookie_handler = HTTPCookieProcessor()
# opener = build_opener(cookie_handler)
#
# req = Request(url)
# res = opener.open(req)
#
# print(res.info())
# print(res.read().decode('utf-8'))
#
# print('-----'*30)
# # second request (POST)
#
# data = "language=python&framework=django"
# encData = bytes(data, encoding='utf-8')
#
# req = Request(url, encData)
# res = opener.open(req)
#
# print(res.info())
# print(res.read().decode('utf-8'))
#
#
# # 예제 2-6 : urlopen() 함수 - ProxyHandler 및 ProxyBasicAuthHandler 클래스로 프록시 처리
# # 프록시 서버가 필요하니 실습은 생략하고 주석 설명으로 코드 이해 (복습)
#
# import urllib.request
#
# url = 'http://www.example.com'
# proxyServer = "http://www.proxy.com:3128/"
#
# # 프록시 서버를 통해 웹 서버로 요청을 보낸다.
# proxy_handler = urllib.request.ProxyHandler({'http':proxyServer})
#
# # 프록시 서버에 대한 인증을 처리한다.
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# ## add_password은 타이핑 시 목록에 나오지 않아서 파이썬 공홈에 가보니 있는 메서드임... 왜 안 나올까
#
# # 2개의 핸들러를 오프너에 등록한다.
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
#
# # 디폴트 오프너로 지정하면, (urlopen()함수로 요청을 보낼 수 있다)
# urllib.request.install_opener(opener)
#
# # opener.open() 대신에 urlopen()을 사용했다.
# f = urllib.request.urlopen(url)
#
# print("getur():", f.geturl())
# print(f.read().decode('utf-8'))
#
# # < 2.2.3 urllib.request 모듈 예제 > 의 < 예제 2-7 > 는 별도 파일로 생성

# 2.2.4 http.client 모듈
# 예제 2-8 : http.client 모듈 사용 - GET 방식 요청
# >python

from http.client import HTTPConnection

host = 'www.example.com'
conn = HTTPConnection(host)
conn.request('GET', '/')  # url을 넣는 두 번째 인자에 왜 '/'만 넣는 걸까? (질문)
r1 = conn.getresponse()
print(r1.status, r1.reason)  # 200 OK가 출력됨

data1 = r1.read()

conn.request('GET', '/')  # 두 번째 요청, 왜 요청을 또하는 거지?
r2 = conn.getresponse()
print(r2.status, r2.reason)  # 역시나 200 OK

data2 = r2.read()
print(data2.decode())  # HTML 파일이 출력된다

conn.close()



# 예제 2-9 : http.client 모듈 사용 - HEAD 방식 요청

from http.client import HTTPConnection
conn = HTTPConnection('www.example.com')
conn.request('HEAD', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.read()
print(len(data))  # 0 출력
print(data == b'')  # True 출력


# 예제 2-10 : http.client 모듈 사용 - POST 방식 요청

from http.client import HTTPConnection
from urllib.parse import urlencode

host = '127.0.0.1:8000'  # 포트번호는 호스트에 포함되는 개념인 건가? (질문)
params = urlencode({
    'language': 'python',
    'name': '김석훈',
    'email': 'shkim@naver.com'
})

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain',
}

conn = HTTPConnection(host)
conn.request('POST', '', params, headers)
resp = conn.getresponse()
print(resp.status, resp.reason)

data = resp.read()
print(data.decode('utf-8'))

conn.close()


# 예제 2-11 : http.client 모듈 사용 - PUT 방식 요청
# > notepad 2-11.py 에 별도로.


# 여기까진 실습도 완료. 이 후엔, 책을 우선 읽은 뒤 실습하면서 이론을 한 번 더 복습하면서, 살습한 소스 코드를 깃헙에 올리기로.210208
