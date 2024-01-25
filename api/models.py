from django.db import models
import uuid
# Create your models here.


def gen_token():
    return f"native-ai-rembg-{uuid.uuid4()}"


class MobileApp(models.Model):
    package_name = models.CharField(max_length=500, blank=True)
    token = models.CharField(max_length=100, blank=True, default=gen_token)
    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    token_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=2, null=False)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    flag = models.FileField(null=True, blank=True, upload_to="flags/4x3/")

    def __str__(self):
        return f"{self.code}"