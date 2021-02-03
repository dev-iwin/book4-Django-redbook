# ch2 - 2. 웹 클라이언트 라이브러리

# # 2.2.1 urllib.parse 모듈
# from urllib.parse import urlparse
# result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
# print(result)

# # 2.2.2 urllib.request module
# # 1 urlopen() 함수 - GET 방식 요청
# from urllib.request import urlopen
# f = urlopen("http://example.com")
# print(f.read(500).decode('utf-8'))
#
# '''
# HTTP GET 방식을 디폴트로 사용하여 웹 서버에 요청한 프로그램.
# 웹 브라우저와 다르게, html 형식의 데이터를 해석하지 않고 그대로 보여줌.
# <!doctype html>부터, html태그, head태그, body태그 전부.

# 위와 같은 명령을 쉘 프롬프트에서는 이렇게 하면 바로 실행 가능.
# >python -c "import urllib.request print(urllib.request.urlopen('http://www.example.com').read(500).decode('utf-8))"
#
# 2 urlopen() 함수 - POST 방식 요청 예제는 장고 프로젝트를 생성한 후 그 서버에서 진행 예정 (종종 그렇게 될 예정)
#'''


