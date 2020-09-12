from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

# class Signup(models.Model):
#     Role = (
#     ("Supervisor", "SV"),
#     ("Teachers", "T"),
#     ("Student", "S"),
# )
#     username = models.OneToOneField(User, on_delete=models.CASCADE, max_length=150)
#     email = models.EmailField()
#     password1 = models.CharField(max_length=25)
#     password2 = models.CharField(max_length=25)
#     role = models.CharField(choices=Role, max_length=50)


#     def __str__(self):
#         return self.email
    
class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3
    ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (ADMIN, 'admin'),
  )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    roles = models.ManyToManyField(Role)