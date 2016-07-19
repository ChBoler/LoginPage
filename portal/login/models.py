from django.db import models

# Dummy test class for permissions
class UserPermissions(models.Model):
    class Meta:
        permissions = [
            ("can_see_vm", "VM Permission")
        ]

