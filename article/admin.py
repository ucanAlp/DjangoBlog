from django.contrib import admin
from .models import Article,comment
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display=["author","title","created_date"]
	list_display_links=["title","author","created_date"]
	search_fields=["title"]
	list_filter=["created_date"]
	class Meta:
		model = Article	
admin.site.register(comment)