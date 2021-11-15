from django.db import models


class UserEmail(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.email)


class Feedback(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)

    def __str__(self) -> str:
        return str(self.first_name)


class Mailing(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)
    sent = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.subject)
