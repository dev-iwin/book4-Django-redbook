# # < 2.2.3 urllib.request 모듈 예제 > 의 < 예제 2-7 > 210207
# # 특정 웹 사이트에서 이미지만을 검색하여 그 리스트를 보여주는 코드
# # urlopen() 함수를 주로 사용했으며, 추가적으로 html.parser 모듈의 HTMLPaser 클래스를 사용

from urllib.request import urlopen
from html.parser import HTMLParser

class ImagePaser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = ImagePaser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    return dataSet

def main():
    url = "http://www.google.co.kr"

    with urlopen(url) as f:
        charset = f.info().get_param('charset')
        data = f.read().decode(charset)

    dataSet = parse_image(data)

    print("\n>>>>>>>> Fetch Images from", url)
    print('\n'.join(sorted(dataSet)))

if __name__ == '__main__':
    main()
