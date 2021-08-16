from django.urls import path
from . import views
from galaksiya_app.views import *

urlpatterns = [
    path("", views.index, name="index"),

]