from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="ratings")
    score = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
