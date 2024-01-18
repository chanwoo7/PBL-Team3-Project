import os

from django.db import models
from django.conf import settings
# Create your models here.


# 광고
class Ad(models.Model):
    # 열거형 첫 번째는 db 저장 값. 쿼리 및 결과 출력에 사용
    # 열거형 두 번째는 폼에 보이는 값

    # TYPE_CHOICES = [
    #     ('image', '사진'),
    #     ('video', '동영상'),
    #     ('banner', '배너'),
    # ]
    TARGET_GENDER_CHOICES = [
        ('남', '남성'),
        ('여', '여성'),
        ('없음', '없음'),
    ]

    id = models.AutoField(primary_key=True)
    adv_name = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    type = models.CharField(max_length=10)
    start_time = models.DateField()
    end_time = models.DateField()
    ad_price = models.IntegerField()
    target_age = models.IntegerField()
    target_gender = models.CharField(max_length=2, choices=TARGET_GENDER_CHOICES, default='없음')


# 미디어
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ad')
    desc = models.CharField(max_length=20)

    def delete(self, *args, **kwargs):
        super(Media, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))


# 광고주
class Adv(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    location = models.CharField(blank=True, max_length=50)
    verified = models.BooleanField(default=False)


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


# 광고-사용자 차단 관련 모델
'''
# 차단 유저 아이디
class BlockedUser(models.Model):
    id = models.IntegerField(primary_key=True)


# 차단 정보 - Ad DB
class Block(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BlockedUser, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()


# 유저 아이피
class User(models.Model):
    ip = models.IntegerField(primary_key=True)


# 차단 정보 - Analyze DB
class BlockInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_id = models.ForeignKey(AdAnlz, on_delete=models.CASCADE)
    is_banned = models.BooleanField(default=False)
'''