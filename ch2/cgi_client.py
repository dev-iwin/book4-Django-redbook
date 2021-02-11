# 예제 2-15 CGI 웹 서버 시험용 클라이언트
# ch2>notetpad cgi-client.py

from urllib.request import urlopen
from urllib.parse import urlencode

url = "http://127.0.0.1:8888/cgi-bin/script.py"
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com',
}
encData = urlencode(data)
postData = encData.encode('ascii')

f = urlopen(url, postData)  # POST 방식
print(f.read().decode('cp949'))

