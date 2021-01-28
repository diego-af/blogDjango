from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','author','publicado','status')
    list_filter =('status','craido','publicado','author',)
    search_fields = ('titulo','conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'publicado'
    raw_id_fields =('author',)