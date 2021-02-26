import json

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from whiteboard.models import Lift, Movement


class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = (
            "id",
            "name",
            "weight",
            "reps",
            "one_rep_max",
            "fake_one_rep",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "labels" in self.fields:
            raise RuntimeError(
                "You cant have labels field defined while using LiftSerializer"
            )

        self.fields["labels"] = SerializerMethodField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["created_at"] = instance.created_at.strftime("%B %d, %Y")
        representation["fake_one_rep"] = f"{instance.fake_one_rep:.1f}"
        return representation

    def get_labels(self, *args):
        return {
            field.name: field.verbose_name
            for field in self.Meta.model._meta.get_fields()
            if field.name in self.fields
        }


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ("name",)
        read_only_fields = ("name",)
