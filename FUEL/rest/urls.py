from django.urls import path, include
from rest_framework import routers
from . import views
from .views import GasApiViewSet

router = routers.DefaultRouter()
router.register('gasolina',views.GasApiViewSet)

urlpatterns = [
    path('',include(router.urls))
]