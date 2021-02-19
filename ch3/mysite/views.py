from django.views.generic.base import TemplateView
from django.apps import apps

#---- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books']  # 이렇게 하나하나 전달해줘야 하나? 기본으로 제공되는 리스트 없나?
        # 이런 걸 하드코딩 한다고 하는 거구나. 난 유연한 게 좋고, 장고가 이를 지원해준다.
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context
