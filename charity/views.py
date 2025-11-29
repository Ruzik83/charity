from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HelpRequest, Media
from .serializers import HelpRequestSerializer

def home(request):
    return render(request, 'base.html')

def services(request):
    return render(request, 'services.html')

def help_view(request):
    approved_requests = HelpRequest.objects.filter(is_approved=True)
    return render(request, 'help.html', {'requests': approved_requests})

def help_request_detail(request, pk):
    req = get_object_or_404(HelpRequest, pk=pk, is_approved=True)
    media_files = Media.objects.filter(help_request=req)
    return render(request, 'help_detail.html', {'req': req, 'media_files': media_files})

class PublicHelpRequestsAPIView(APIView):
    def get(self, request):
        requests = HelpRequest.objects.filter(is_approved=True)
        serializer = HelpRequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HelpRequestDetailAPIView(APIView):
    def get(self, request, pk):
        help_request = get_object_or_404(HelpRequest, pk=pk, is_approved=True)
        serializer = HelpRequestSerializer(help_request)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MediaListAPIView(APIView):
    def get(self, request):
        approved_requests = HelpRequest.objects.filter(is_approved=True)
        media_list = []
        for req in approved_requests:
            if req.image:
                media_list.append({
                    "type": "image",
                    "url": request.build_absolute_uri(req.image.url),
                    "request_id": req.id,
                    "full_name": req.full_name
                })
            if req.video:
                media_list.append({
                    "type": "video",
                    "url": request.build_absolute_uri(req.video.url),
                    "request_id": req.id,
                    "full_name": req.full_name
                })
            related_media = Media.objects.filter(help_request=req)
            for media in related_media:
                media_type = "video" if str(media.file).lower().endswith(".mp4") else "image"
                media_list.append({
                    "type": media_type,
                    "url": request.build_absolute_uri(media.file.url),
                    "request_id": req.id,
                    "full_name": req.full_name
                })
        return Response(media_list, status=status.HTTP_200_OK)

def search_help_requests(request):
    query = request.GET.get('q', '')
    results = HelpRequest.objects.filter(full_name__icontains=query, is_approved=True)
    return render(request, 'help.html', {'requests': results, 'query': query})

def filter_help_requests(request, category):
    filtered = HelpRequest.objects.filter(category__iexact=category, is_approved=True)
    return render(request, 'help.html', {'requests': filtered, 'category': category})

def latest_help_requests(request):
    latest = HelpRequest.objects.filter(is_approved=True).order_by('-created_at')[:10]
    return render(request, 'help.html', {'requests': latest})

def top_help_requests(request):
    top = HelpRequest.objects.filter(is_approved=True).order_by('-donations')[:10]
    return render(request, 'help.html', {'requests': top})

def help_requests_by_date(request, year, month):
    requests = HelpRequest.objects.filter(created_at__year=year, created_at__month=month, is_approved=True)
    return render(request, 'help.html', {'requests': requests, 'year': year, 'month': month})
