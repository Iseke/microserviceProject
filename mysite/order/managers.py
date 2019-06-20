from django.db import models


class OrderManager(models.Manager):
    def for_user(self, user):
        return self.filter(owned_by=user)