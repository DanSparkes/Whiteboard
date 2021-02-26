from django.contrib import admin

from whiteboard.models import Lift, Movement


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
