from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Countries', views.CountryViewset, 'Country')


# urlpatterns = router.urls

urlpatterns = [
    path('api', include(router.urls))
]
