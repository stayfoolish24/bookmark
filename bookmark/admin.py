from django.contrib import admin

# 관리자 페이지에 모델을 추가하거나
# 기능을 커스터마이징 하고자 할 때 수정하는 파일

# Register your models here.
from .models import Bookmark

class AdminBookmark(admin.ModelAdmin):
    list_display = ['id','site_name','url']

admin.site.register(Bookmark, AdminBookmark)
