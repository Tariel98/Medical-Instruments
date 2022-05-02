from django.db import models
from django.utils import timezone


class Contact(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Կապ ադմինիստրատորի հետ'
        verbose_name_plural = 'Կապ ադմինիստրատորի հետ'
