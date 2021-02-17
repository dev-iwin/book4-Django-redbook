from django.shortcuts import render
from django.http import HttpResponseRedirect

# 예제 4-21
from .forms import NameForm

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            # 그외 필요한 명령들 ...
            return HttpResponseRedirect('/thanks/')

    else: # POST가 아니면 무조건 GET임 = 사용자에게 처음 보여주는 폼
        form = NameForm()

    return render(request, 'name.html', {'form': form})




# 4.5 클래스형 뷰 ============================================
from django.http import HttpResponse

# 예제 4-25 : 클래스형 뷰 - MyView 정의
from django.views.generic import View

class MyView(View):
    def get(self, request):
        # 뷰 로직
        return HttpResponse('result')


# 예제 4-26 : 함수형으로 HTTP GET 메소드 코딩 (앞 예제와 같은 동작)
def my_view(request):
    if request.method == 'GET':
        # 뷰 로직
        return HttpResponse('result')

# 예제 4-26 : 클래스형 뷰로 HTTP HEAD 메소드 코딩
# books 앱의 models.py의 Book클래스, views.py에 BookListView클래스




