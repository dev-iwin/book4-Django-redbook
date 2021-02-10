# 2.3.4 CGIHTTPRequestHandler 클래스
# 예제 2-14 CGI 웹 서버 시험용 CGI 스크립트

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print("Content-Type: text/plain")
print()

print("Welcome... CGI Scripts")
print("name is", name)
print('email is', email)
print('url is', url)
