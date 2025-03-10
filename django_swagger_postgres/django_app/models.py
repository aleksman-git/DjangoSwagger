from django.db import models


class Login(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=True, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('email',)
        verbose_name = 'mail'
        verbose_name_plural = 'mails'

"""
class Password(models.Model):
    pw = models.CharField(max_length=100, null=True,blank=True)
    login_id = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.pw

    class Meta:
        verbose_name = 'password'
        verbose_name_plural = 'passwords'
        ordering = ('pw',)
"""
