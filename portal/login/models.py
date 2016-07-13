from django.db import models

# Dummy test class for permissions
class TestPermission(models.Model):
    class Meta:
        permissions = [
            ("can_see", "Arbitrary Permission")
        ]

