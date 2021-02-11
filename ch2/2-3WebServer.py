# 2.3.1 간단한 웹 서버
# 예제 2-13 : 간단한 웹 서버
# >notepad my_httpserver.py 별도 파일에 저장

# 예제 2-13과 2-14 사이
# 2.3.3 SimpleHTTPRequestHandle
# >python -m http.server 8888
# 그 후 http://127.0.0.1:8888/
# 또는 http://localhost:8888/

# 2.3.4 CGIHTTPRequestHandler 클래스
# 예제 2-14 CGI 웹 서버 시험용 CGI 스크립트
# cgi-server>notepad cgi-bin\scripts.py 에 저장

# 예제 2-15 CGI 웹 서버 시험용 클라이언트
# ch2>notetpad cgi-client.py 에 저장

# xxxHTTPServer 각 모듈에, 별도의 코딩 없이 기동할 수 있도록 test() 함수를 정의하고 있음
# 예, CGI 처리가 가능한 CGTHTTPServer 기동을 위한 test()함수 실행 @ CLI
# >python -c "import CGIHTTPServer.test()" 8888

# 2.4.4 wsgiref.simple_server 모듈
# 예제 2-16 : WSGI 서버
