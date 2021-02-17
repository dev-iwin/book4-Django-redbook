from django.shortcuts import render
from django.http import HttpResponse

# 예제 4-26 : 클래스형 뷰로 HTTP HEAD 메소드 코딩
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        # publication_date가 Book의 멤버인지, 필드의 인지?(질문) self.get_queryset().latest()를 검색해봐야겠군
        response = HttpResponse('')
        # RFC 1123 date 포맷   # 이건 뭐지? (질문)
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

# =======================================================================================================