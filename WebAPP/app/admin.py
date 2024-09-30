from django.contrib import admin
from app.models import *
# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')
    fields = [('title', 'cost', 'size'), 'description', 'image', 'reviews']
    search_fields = ('title',)
    list_filter = ('title', 'cost')


admin.site.register(Post)
