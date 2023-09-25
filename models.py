from django.db import models

# Create your models here.
class hel(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=122, null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=122, null=True)

    def __str__(self):
        return f"{self.name}"
