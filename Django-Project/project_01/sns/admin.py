from django.contrib import admin
from .models import Posting, Comment


class PostingModelAdmin(admin.ModelAdmin):
    # readonly_fields에는 원래대로라면 안보일 항목인데 보이도록 함
    readonly_fields = ('image_thumbnail','create_at','updated_at')
    # admin 페이지의 리스트 목록에서 보여줄 항목
    list_display = ('id','content','create_at','updated_at')
    # admin 페이지의 리스트 칼럼 중 클릭리 가능해질 칼럼
    list_display_links = ('id','content')
# Register your models here.
admin.site.register(Posting,PostingModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','updated_at')
    list_display = ('id','content','create_at','updated_at')
    list_display_links = ('id','content')

admin.site.register(Comment,CommentModelAdmin)