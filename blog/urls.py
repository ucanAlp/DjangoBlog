from django.contrib import admin
from django.urls import path,include
from article.views import index
from article import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about/', views.about),
    path('detail/<int:id>', views.detail,name="detail"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('tamamla/',views.tamamla),
    path('iletisim/',views.iletisim)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

