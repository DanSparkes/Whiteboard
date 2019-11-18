from django.db import models
from django.contrib.auth.models import User


class Movement(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Lift Name")

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Exercise Name")

    def __str__(self):
        return self.name


class WodType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="WOD Type")

    def __str__(self):
        return self.name


class WOD(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="User", related_name="wods"
    )
    name = models.CharField(max_length=100, unique=True, verbose_name="WOD Name")
    wod_type = models.ForeignKey(
        WodType, on_delete=models.CASCADE, to_field="name", verbose_name="WOD Type"
    )
    rounds = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Set")

    def __str__(self):
        return self.name


class RepScheme(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        to_field="name",
        verbose_name="Exercise Name",
    )
    wod = models.ForeignKey(
        WOD, on_delete=models.CASCADE, to_field="name", verbose_name="WOD Name"
    )
    reps = models.IntegerField(verbose_name="Reps")
    weight = models.IntegerField(blank=True, null=True, verbose_name="Weight Lifted")


# class WodScore(models.Model):
#     wod = models.ForeignKey(
#         WOD, on_delete=models.CASCADE, to_field="name", verbose_name="WOD Name"
#     )
#     rep_score = models.IntegerField(blank=True, null=True, verbose_name="Score")
#     time_score = models.DurationField(blank=True, null=True, verbose_name="Score")
