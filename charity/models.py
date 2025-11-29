from django.db import models
from rest_framework.views import APIView
from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='campaign_images/', null=True, blank=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HelpRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # <-- AGAR ishlatmoqchi bo‘lsangiz
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # <-- AGAR ishlatmoqchi bo‘lsangiz

    def __str__(self):
        return self.full_name




class MediaAPIView(APIView):
    def get(self, request):
        request_id = request.GET.get('request_id')
        if request_id:
            medias = Media.objects.filter(request_id=request_id)
        else:
            medias = Media.objects.all()

        serializer = MediaSerializer(medias, many=True, context={'request': request})
        return Response(serializer.data)

class Media(models.Model):
    help_request = models.ForeignKey(HelpRequest, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"Media for {self.help_request.name}"