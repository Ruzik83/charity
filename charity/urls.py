from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, help_view, services, help_request_detail, PublicHelpRequestsAPIView, MediaListAPIView

urlpatterns = [
    path('', home, name='home'),
    path('help/', help_view, name='help'),
    path('services/', services, name='services'),
    path('api/helprequests/', PublicHelpRequestsAPIView.as_view(), name='api_help_requests'),
    path('help/<int:pk>/', help_request_detail, name='help_request_detail'),
    path('api/media/', MediaListAPIView.as_view(), name='api_media_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
