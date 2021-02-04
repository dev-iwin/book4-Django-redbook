# ch2 - 2. 웹 클라이언트 라이브러리

# 2.2.1 urllib.parse 모듈
from urllib.parse import urlparse
result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
print(result)

# 2.2.2 urllib.request module
# 1 urlopen() 함수 - GET 방식 요청
from urllib.request import urlopen
f = urlopen("http://example.com")
print(f.read(500).decode('utf-8'))

'''
HTTP GET 방식을 디폴트로 사용하여 웹 서버에 요청한 프로그램.
웹 브라우저와 다르게, html 형식의 데이터를 해석하지 않고 그대로 보여줌.
<!doctype html>부터, html태그, head태그, body태그 전부.

위와 같은 명령을 쉘 프롬프트에서는 이렇게 하면 바로 실행 가능.
>python -c "import urllib.request print(urllib.request.urlopen('http://www.example.com').read(500).decode('utf-8))"

2.2.2 urlopen() 함수 - POST 방식 요청 예제는 장고 프로젝트를 생성한 후 그 서버에서 진행 예정 (종종 그렇게 될 예정)
'''

# 2.2.2 urlopen() 함수 - POST 방식 요청
# >python
from urllib.request import urlopen
data = "language=python&framework=django"
f = urlopen(" http://127.0.0.1:8000/", bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))


# 2.2.3 ulropen()함수 - Request 클래스로 요청 헤더 지정
# Request 객체를 생성한 뒤, add_header() 메서드 추가해서 웹서버에 요청보내기
# >python
from urllib.request import urlopen, Request
from urllib.parse import urlencode
data = "language=python&framework=django"
f = urlopen(" http://127.0.0.1:8000/", bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))

url = 'http://127.0.0.1:8000/'
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com'
}
encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data=postData)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(500).decode('utf-8'))

# 2.2.4 urlopen()함수 - HTTPBasicAuthHandler 클래스로 인증 요청
# >python
from urllib.request import HTTPBasicAuthHandler, build_opener
auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm='ksh', user='shkim', passwd='shkimadmin', uri='http://127.0.0.1:8000/auth/')
opener = build_opener(auth_handler)
resp = opener.open('http://127.0.0.1:8000/auth/')
print(resp.read().decode('utf-8'))

# 여기까진 실습도 완료. 이 후엔, 책을 우선 읽은 뒤 실습하면서 이론을 한 번 더 복습하면서, 살습한 소스 코드를 깃헙에 올리기로.