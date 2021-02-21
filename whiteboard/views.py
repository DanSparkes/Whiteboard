from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from whiteboard.models import Lift, Movement, WOD, WodScore
from whiteboard.serializers import LiftSerializer, MovementSerializer, WodScoreSerializer


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/accounts/login")
    return render(request, "frontend/index.html")

class LiftListCreate(generics.ListCreateAPIView):
    queryset = Lift.objects.all().order_by("-created_at")
    serializer_class = LiftSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = (
            self.get_queryset().filter(user=request.user).order_by("-created_at")
        )[:10]
        serializer = LiftSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        lifter = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(user=lifter)


class LiftList(generics.ListAPIView):
    queryset = Lift.objects.all().order_by("-created_at")
    serializer_class = LiftSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, liftname):
        queryset = (
            self.get_queryset()
            .filter(name__name__exact=liftname, user=request.user)
            .order_by("-created_at")
        )[:10]
        serializer = LiftSerializer(queryset, many=True)
        return Response(serializer.data)


class MovementList(generics.ListAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    permission_classes = (IsAuthenticated,)


class WODListCreate(generics.ListCreateAPIView):
    queryset = WodScore.objects.all()
    serializer_class = WodScoreSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = (self.get_queryset().all())[:10]
        serializer = WodScoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        athlete = get_object_or_404(User, id=1)
        return serializer.save(user=athlete)
