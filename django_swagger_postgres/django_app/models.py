from django.db import models


class Login(models.Model):
    email = models.CharField(max_length=50, null=False, blank=True, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'login'
        verbose_name_plural = 'logins'
        ordering = ('email',)



class Password(models.Model):
    pw = models.CharField(max_length=100, null=True,blank=True)
    login_id = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.pw

    class Meta:
        verbose_name = 'password'
        verbose_name_plural = 'passwords'
        ordering = ('pw',)

