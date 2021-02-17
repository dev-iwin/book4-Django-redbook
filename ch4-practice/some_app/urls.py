from django.urls import path
# from .views import AboutView  # 예제 4-29
from django.views.generic import TemplateView

urlpatterns = [
    # path('about/', AboutView.as_view()),  # 예제 4-29
    path('about/', TemplateView.as_view(template_name="about.html")),  # 예제 4-30 : 이렇게 하면 예제 4-29의 뷰 클래스도 필요 없음
]