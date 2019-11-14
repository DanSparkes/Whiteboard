from django.db import models
from django.contrib.auth.models import User

from utils import WorkoutTypes


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
    weight = models.IntegerField(blank=True, null=True, verbose_name="Weight Lifted")
    reps = models.IntegerField(blank=True, null=True, verbose_name="Reps")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Set")


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Exercise Name")
    has_weight = models.BooleanField(default=False)


class WOD(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name="WOD Name")
    wod_type = models.IntegerField(
        choices=WorkoutTypes.choices(), default=WorkoutTypes.FOR_TIME
    )
    exercises = models.ManyToManyField(Exercise)
    rounds = models.IntegerField(default=1)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def get_customer_type_label(self):
        return WorkoutTypes(self.wod_type).name.title()
