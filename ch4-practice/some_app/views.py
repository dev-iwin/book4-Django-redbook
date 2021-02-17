from django.shortcuts import render

# 예제 4-29 : TemplateView 상속 ================
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"  # 한 줄로 끝. urls.py에서 뷰 지정하기 = 예제 4-30
