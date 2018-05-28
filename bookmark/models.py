from django.db import models

# 내가 데이터베이스에 어떤 데이터를 어떻게 저장할 것이냐?
# O.R.M (object related mapping?)


# Create your models here.

# Models.py -> view.py -> urls.py -> Template

# 하나의 테이블을 하나의 모델로 묘사한다.
# 모델은 class로 구현한다.


class Bookmark(models.Model): #models.Model이 ORM기능을 상속한다.
    # 하나의 필드를 만든다.
    # 컬럼 이름 = 컬럼 종류(제약조건)
    site_name = models.CharField(max_length=100)
    url = models.URLField('url')

    # 모델의 옵션
    class Meta:
        ordering = ['site_name'] #'-site_name' 내림차순 일 경우 마이너스

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        from django.urls import reverse
        # http://localhost:8000/bookmark/detail/4
        return reverse('bookmark:detail', args=[str(self.id)])
