from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from lifts.models import Lift, Movement
from lifts.serializers import LiftSerializer, MovementSerializer


class LiftListCreate(generics.ListCreateAPIView):
    queryset = Lift.objects.all().order_by("-created_at")[:10]
    serializer_class = LiftSerializer
    permission_classes = (IsAuthenticated,)


class LiftList(generics.ListAPIView):
    queryset = Lift.objects.all().order_by("-created_at")
    serializer_class = LiftSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, liftname):
        queryset = (
            self.get_queryset()
            .filter(name__name__exact=liftname)
            .order_by("-created_at")
        )[:10]
        serializer = LiftSerializer(queryset, many=True)
        return Response(serializer.data)


class MovementListCreate(generics.ListAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    permission_classes = (IsAuthenticated,)
