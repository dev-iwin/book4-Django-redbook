"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import views  # 현재 경로를 절대경로로 이렇게 표현할 수 있는 게 맞아? . 해야 하는 거 아니야?

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls')),  # polls 앱 내부의 urls.py로 연결하는 코드 (계층구성, 확장에 용이)
    path('books/', include('books.urls')),

]
''' path('polls/', views.index, name='index'),
   path('polls/<int:question_id>/', views.detail, name='detail'),
   path('polls/<int:question_id>/results/', views.results, name='results'),
   path('polls/<int:question_id>/vote/', views.vote, name='vote'),'''

