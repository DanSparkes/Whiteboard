from django.contrib import admin

from lifts.models import Lift, Movement

admin.site.register(Lift)


class MovementAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]


admin.site.register(Movement, MovementAdmin)
