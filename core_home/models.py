from django.db import models

from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100, default="Husayn")
    role = models.CharField(max_length=100, default="Backend Developer")
    description = models.TextField()
    stack = models.CharField(max_length=200, default="Django • Python • JS")
    country = models.CharField(max_length=100, default="Uzbekistan")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=2)  # ✅ yangi

    def __str__(self):
        return self.name