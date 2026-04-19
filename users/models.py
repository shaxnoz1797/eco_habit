from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver



class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username or str(self.telegram_id)




class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    is_done = models.BooleanField(default=False)

    streak = models.IntegerField(default=0)
    last_done_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name




class User(AbstractUser):
    eco_score = models.IntegerField(default=0)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eco_score = models.IntegerField(default=0)



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)