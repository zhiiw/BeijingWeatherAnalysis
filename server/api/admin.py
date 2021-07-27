from django.contrib import admin

# Register your models here.
from .models import User, Comment


class UserAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["username", "last_login"]
    list_per_page = 8 #一页显示多少条
    search_fields = ['username'] #过滤器


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "createTime", "user_id"]
    list_per_page = 15  # 一页显示多少条
    list_filter = ['user_id']  # 过滤器


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.site_header = 'ShengHua Talents administration'
admin.site.site_title = 'ShengHua Talents'

