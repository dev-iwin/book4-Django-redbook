from django.shortcuts import render
from django.http import HttpResponseRedirect
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