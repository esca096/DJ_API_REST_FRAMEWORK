from django.urls import path
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

"""
default router est utilisé pour les opérations CRUD
simple router est utilisé pour les opérations de lecture
"""


router = DefaultRouter()
router.register('v1/product', ProductViewSet, basename='product')

urlpatterns = router.urls

