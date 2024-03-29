"""whiteboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from whiteboard.views import LiftList, LiftListCreate, MovementList, index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/lifts/", LiftListCreate.as_view(), name="lift_list"),
    re_path(
        r"api/lifts/(?P<liftname>[\w|\W]+)/$", LiftList.as_view(), name="single_lift"
    ),
    path("api/movements/", MovementList.as_view(), name="movement_list"),
]
