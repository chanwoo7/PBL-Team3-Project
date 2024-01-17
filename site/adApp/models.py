import os

from django.db import models
from django.conf import settings
# Create your models here.


# 광고주
class Adv(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50, blank=True)
    verified = models.BooleanField(default=False)


# 광고
class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    adv_id = models.ForeignKey(Adv, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    type = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ad_price = models.IntegerField(default=0)


# 광고 분석
class AdAnlz(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=500)
    num_of_shows = models.IntegerField(default=0)
    total_revenue = models.IntegerField(default=0)
    num_of_redirects = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    previews = models.IntegerField(default=0)


# 유저
class User(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=2)
    age = models.IntegerField(default=0)
    lang = models.CharField(max_length=10)
    # 필요 시 추가


# 미디어 테스트 테이블
class MediaTest(models.Model):
    file = models.FileField(blank=True, upload_to='ad/%Y%m%d')
    desc = models.CharField(blank=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        super(MediaTest, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))


# 광고-사용자 차단 관련 모델
'''
# 차단 유저 아이디
class BlockedUser(models.Model):
    id = models.IntegerField(primary_key=True)


# 차단 정보 - Ad DB
class Block(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BlockedUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


# 유저 아이피
class User(models.Model):
    ip = models.IntegerField(primary_key=True)


# 차단 정보 - Analyze DB
class BlockInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_id = models.ForeignKey(AdAnlz, on_delete=models.CASCADE)
    is_banned = models.BooleanField(default=False)
'''
