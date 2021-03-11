from django.db import models
from django.conf import settings
from datetime import datetime
import os


def profile_directory_photo(instance, filename):
    if instance.photo:
        if os.path.exists(instance.photo.path):
            os.remove(instance.photo.path)

    now = datetime.now()

    return 'images/users/{year}/{month}/{day}/{filename}'\
        .format(
            year=now.year,
            month=now.month,
            day=now.day,
            username=instance.user.username,
            filename=filename
        )


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=profile_directory_photo, blank=True)


    def __str__(self):
        return f'Profile for user {self.user.username}'