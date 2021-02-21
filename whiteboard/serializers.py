import json

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from whiteboard.models import (
    Lift,
    Movement,
    WOD,
    WodType,
    Exercise,
    RepScheme,
    RepWeight,
    WodScore,
)


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
        return {
            field.name: field.verbose_name
            for field in self.Meta.model._meta.get_fields()
            if field.name in self.fields
        }


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ("name",)
        read_only_fields = "name"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ("name",)
        read_only_fields = "name"


class WodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodType
        fields = ("name",)
        read_only_fields = "name"


class RepWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepWeight
        fields = ("weight",)


class RepSchemeSerializer(serializers.ModelSerializer):
    weight = RepWeightSerializer(source="repscheme_set")

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
            "exercises",
        )

    def create(self, validated_data):
        exercises_data = validated_data.pop("repscheme_set")
        wod = WOD.objects.create(**validated_data)
        for exercise_data in exercises_data:
            RepScheme.objects.create(wod=wod, **exercise_data)
        return wod


class WodScoreSerializer(serializers.ModelSerializer):
    wod = WODSerializer()

    class Meta:
        model = WodScore
        fields = (
            "user",
            "wod",
            "rep_score",
            "time_score",
            "notes",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super(WodScoreSerializer, self).__init__(*args, **kwargs)

        if "labels" in self.fields:
            raise RuntimeError(
                "You cant have labels field defined while using WodScoreSerializer"
            )

        self.fields["labels"] = SerializerMethodField()

    def get_labels(self, *args):
        return {
            field.name: field.verbose_name
            for field in self.Meta.model._meta.get_fields()
            if field.name in self.fields
        }

    def create(self, validated_data):
        print(f"validated_data = {validated_data}")
        wod_data = validated_data.pop("wod")
        import pdb

        pdb.set_trace()

        wod, created = WOD.objects.get_or_create(
            name=wod_data.get("name", ""),
            wod_type=wod_data.get("wod_type", ""),
            rounds=wod_data.get("rounds", ""),
        )
        exercises_data = wod_data.pop("repscheme_set")
        for exercise_data in exercises_data:
            weight_data = exercise_data.pop("weight")
            rep_scheme, created = RepScheme.objects.get_or_create(
                wod=wod, **exercise_data
            )
            RepWeight.objects.get_or_create(
                rep_scheme=rep_scheme, weight=weight_data.get("weight", 0)
            )
        return WodScore.objects.create(**validated_data, wod=wod)
