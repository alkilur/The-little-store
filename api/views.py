
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import BasketItem, Product
from products.serializers import BasketItemSerializer, ProductsSerializer


class ProductsModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy'):
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class BasketItemModelViewSet(ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def create(self, request):
        try:
            product_id = request.data['product_id']
            product = Product.objects.filter(id=product_id)

            if product:
                obj, is_created = BasketItem.create_or_update(product_id, self.request.user)
                status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
                serializer = self.get_serializer(obj)
                return Response(serializer.data, status=status_code)
            else:
                return Response({'product_id': 'There is no product with this ID.'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'product_id': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
