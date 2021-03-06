from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    push_token = models.CharField(max_length=200, blank=False, null=True)

    class Meta:
        db_table = "account"
