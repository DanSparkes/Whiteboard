from django.contrib import admin

from whiteboard.models import Lift, Movement, Exercise, WodType, WOD, RepScheme, RepWeight


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
    list_display = [
        "name",
        "wod_type",
    ]


admin.site.register(WOD, WODAdmin)


class RepSchemeAdmin(admin.ModelAdmin):
    list_display = ["exercise", "wod", "reps"]


admin.site.register(RepScheme, RepSchemeAdmin)


class RepWeightAdmin(admin.ModelAdmin):
    list_display = ["rep_scheme", "weight"]


admin.site.register(RepWeight, RepWeightAdmin)

