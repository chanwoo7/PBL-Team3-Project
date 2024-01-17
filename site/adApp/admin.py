from django.contrib import admin

# Register your models here.


# ------------------------------ #
# DB 관리
from django.contrib import admin
from .models import *

admin.site.register(Adv)
admin.site.register(Ad)
admin.site.register(AdAnlz)
admin.site.register(User)
# ------------------------------ #
