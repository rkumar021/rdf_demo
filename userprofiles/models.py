from django.db import models

class Userroles(models.Model):
    roles = (
    ("admin", "Admin"),
    ("user", "User"),
)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, max_length=150)
    email = models.EmailField()
    role = models.CharField(choices=roles, max_length=25)
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)