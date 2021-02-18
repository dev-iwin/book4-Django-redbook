from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View


from .forms import MyForm

# 예제 4-32 : View를 상속한 클래스형 뷰로 폼 처리 =======================
# 함수형 뷰보다 로직별 구분이 잘 되어 가독성 상승
class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.intial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # cleaned_data로 관련 로직 처리
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


# 예제 4-33 : FormView를 상속한 클래스형 뷰로 폼 처리 (앞 예제보다 더 간단) ===
from django.views.generic import FormView

class MyFormView2(FormView):
    form_class = MyForm
    template_name = 'form_template.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        # cleaned_data로 관련 로직 처리
        return super(MyFormView2, self).form_valid(form)