"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from bookmark.views import BookmarkListView

urlpatterns = [
    # http://localhost:8000/admin/
    # 2차 url로 라우팅을 해준다. (앱에게 토스해준다.)
    # 예전 버전을 생각해서 위쪽에는 좁은 범위, 아래쪽으로 내려 올수록 넓은 범위(index)로 하는 것이 좋다. ex) bookmark , admin, '' 순으로 작성
    path('bookmark/',include('bookmark.urls', namespace='bookmark')), # namespace는 주소에서 아파트 이름 같은 역할
    path('admin/', admin.site.urls),
    path('',BookmarkListView.as_view(), name='index'), # name는 주소에서  동호수 같은 역할
    #re_path(),
]
