from django.db import models
from django.utils import timezone

from user.models import UserModel

class MaleFemaleConnectionModel(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(UserModel, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, related_name='to_user', on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_request_sent = models.BooleanField(default=False)
    is_request_accepted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
