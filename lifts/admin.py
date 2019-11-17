from django.contrib import admin

from lifts.models import Lift, Movement, Exercise, WodType, WOD, RepScheme


class LiftAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "name",
        "weight",
        "reps",
        "one_rep_max",
        "fake_one_rep",
    ]


admin.site.register(Lift, LiftAdmin)


class MovementAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]


admin.site.register(Movement, MovementAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]


admin.site.register(Exercise, ExerciseAdmin)


class WodTypeAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]


admin.site.register(WodType, WodTypeAdmin)


class WODAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "rep_score", "time_score"]


admin.site.register(WOD, WODAdmin)


class RepSchemeAdmin(admin.ModelAdmin):
    list_display = ["exercise", "wod", "reps", "weight"]


admin.site.register(RepScheme, RepSchemeAdmin)
