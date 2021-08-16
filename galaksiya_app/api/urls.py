from django.urls import path, include

from galaksiya_app.api.views import ProductListAPIView

urlpatterns = [
    path('list', ProductListAPIView.as_view(),name='list'),

]