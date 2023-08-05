
from django.urls import include, path
from rest_framework import routers

from api.views import BasketItemModelViewSet, ProductsModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductsModelViewSet)
router.register(r'basket_items', BasketItemModelViewSet)


urlpatterns = [
                path('', include(router.urls)),
              ]
