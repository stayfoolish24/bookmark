from django.shortcuts import render,redirect

# 어떤 기능을 만들어 주는 곳
# urls.py 내가 views.py 만든 기능이 어떤 url로 접속했을 때 동작하게 할 것이냐?

# Create your views here.

from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

from django.views.generic.list import ListView
from .models import Bookmark
class BookmarkListView(ListView):
    model = Bookmark


from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookmarkCreateView(CreateView):
    model = Bookmark
    template_name_suffix ='_create' #템플릿 이름 바꾸는 부분
    fields = ['site_name','url'] # 사용자가 입력해야될 부분만 fields에 명시

    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form':form}) # 실패했을 경우 입력할 화면으로 다시 돌려준다.(패스워드 점검해서 2번쓸 때 틀렸을 경우 같은 경우)


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

from django.views.generic.detail import DetailView
class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    from django.urls import reverse_lazy
    model = Bookmark
    success_url = reverse_lazy('bookmark:index') #호출 타이밍에 reverse_lazy가 만들어진다?