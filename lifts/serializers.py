from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lifts.models import Lift, Movement, WOD, WodType, Exercise, RepScheme


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
        super(LiftSerializer, self).__init__(*args, **kwargs)

        if "labels" in self.fields:
            raise RuntimeError(
                "You cant have labels field defined while using LiftSerializer"
            )

        self.fields["labels"] = SerializerMethodField()

    def to_representation(self, instance):
        representation = super(LiftSerializer, self).to_representation(instance)
        representation["created_at"] = instance.created_at.strftime("%B %d, %Y")
        representation["fake_one_rep"] = f"{instance.fake_one_rep:.1f}"
        return representation

    def get_labels(self, *args):
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = "name"
        read_only_fields = "name"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "name"
        read_only_fields = "name"


class WodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodType
        fields = "name"
        read_only_fields = "name"


class RepSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepScheme
        fields = ("exercise", "reps", "weight")


class WODSerializer(serializers.ModelSerializer):
    exercises = RepSchemeSerializer(source="repscheme_set", many=True)

    class Meta:
        model = WOD
        fields = (
            "name",
            "wod_type",
            "rounds",
            "notes",
            "exercises",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super(WODSerializer, self).__init__(*args, **kwargs)

        if "labels" in self.fields:
            raise RuntimeError(
                "You cant have labels field defined while using LiftSerializer"
            )

        self.fields["labels"] = SerializerMethodField()

    def get_labels(self, *args):
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels

    def create(self, validated_data):
        exercises_data = validated_data.pop("repscheme_set")
        wod = WOD.objects.create(**validated_data)
        for exercise_data in exercises_data:
            RepScheme.objects.create(wod=wod, **exercise_data)
        new_exercises = RepScheme.objects.filter(wod=wod)

        existing_wods = WOD.objects.all()
        for old_wod in existing_wods:
            exercises = RepScheme.objects.filter(wod=old_wod)
            # TODO this part doesn't work the way I want it to...
            if exercises == new_exercises:
                wod.delete()
                return old_wod
        return wod
