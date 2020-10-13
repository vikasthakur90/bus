from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)

    def __str__(self):
        return "first_name:"+self.first_name+" username:"+self.username+" email:"+self.email