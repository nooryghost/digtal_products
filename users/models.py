from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.validators import validate_phone_number

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(validators=[validate_phone_number])
    nick_name = models.CharField(max_length=25, blank=True)
    avatar = models.ImageField(blank=True)
    sex = models.BooleanField(null=True, help_text="false is Female and True is Male")
    province = models.ForeignKey(to="Province", null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_profiles"

class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (1, "web"),
        (2, "ios"),
        (3, "android")
    ) 
    
    user = models.ForeignKey(User, related_name="devices", on_delete=models.CASCADE)
    device_uuid = models.UUIDField(null=True)
    last_login = models.DateTimeField(null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=1)
    device_model = models.CharField(max_length=25, blank=True)
    app_version = models.CharField(max_length=25, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_device"
        unique_together = ["user", "device_uuid"]

class Province(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name