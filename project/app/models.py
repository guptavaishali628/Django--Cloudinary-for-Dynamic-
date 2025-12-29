from django.db import models
# for dynamic cloudinary
from cloudinary_storage.storage import MediaCloudinaryStorage , RawMediaCloudinaryStorage, VideoMediaCloudinaryStorage

# Create your models here.

class Student(models.Model):
    Image=models.ImageField(upload_to='image', storage=MediaCloudinaryStorage())
    video=models.FileField(upload_to='video', storage=VideoMediaCloudinaryStorage())
    audio=models.FileField(upload_to='audio', storage=VideoMediaCloudinaryStorage())
    file=models.FileField(upload_to='file', storage=RawMediaCloudinaryStorage())