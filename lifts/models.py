from django.db import models
from django.contrib.auth.models import User


class Movement(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Lift Name")


class Lift(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="User", related_name="lifts"
    )
    name = models.ForeignKey(
        Movement, on_delete=models.CASCADE, to_field="name", verbose_name="Lift Name"
    )
    one_rep_max = models.IntegerField(blank=True, null=True, verbose_name="One Rep Max")
    fake_one_rep = models.FloatField(
        blank=True, null=True, verbose_name="Theoretical One Rep"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Set")

