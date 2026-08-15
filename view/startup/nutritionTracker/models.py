from django.db import models
from django.db.models import CASCADE


def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'


# Create your models here.
class NutritionFacts(models.Model):
    timestamp = models.DateTimeField()
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    output_json = models.FileField(upload_to=user_directory_path)
