from django.db import models

class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=50, null=False, blank=False)
    user_name = models.CharField(max_length=100, null=False, blank=False)
    user_email = models.EmailField(null=False, blank=False)
    user_age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'NickName: {self.user_nickname} | Email: {self.user_email}'
    
    