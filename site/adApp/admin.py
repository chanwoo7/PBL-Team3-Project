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
# admin.site.register(Media)
# ------------------------------ #


# ------------------------------ #
# Media Setting
from django.utils.safestring import mark_safe


@admin.register(Media)
class POSTAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_tag', 'desc', 'created_at', 'updated_at']
    list_display_links = ['desc']
    list_filter = ['created_at', 'desc']
    search_fields = ['desc']

    def file_tag(self, post):
        # 안전하게 필드명 저장유무를 체크해주자.
        # 필드에 저장된 경로가 없을 경우, url 계산에 실패한다.
        if post.file:
            return mark_safe(f'<img src="{post.file.url}" style="width:50px;" />')
        return None

# ------------------------------ #
