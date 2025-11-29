from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from django.views.i18n import set_language  # Bu yerda to'g'ri import qilamiz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('charity.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Tilni o'zgartirish uchun i18n_patterns qo'shish
urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),  # set_language to'g'ri import qilindi
)
