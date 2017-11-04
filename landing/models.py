from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(default='')
    name = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=48, null=False)
    address = models.CharField(max_length=128, null=False, default='')
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
