
from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrdersListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
                path('', OrdersListView.as_view(), name='orders_list'),
                path('order/<int:pk>', OrderDetailView.as_view(), name='order'),
                path('create/', OrderCreateView.as_view(), name='create'),
                path('success/', SuccessTemplateView.as_view(), name='success'),
                path('canceled/', CanceledTemplateView.as_view(), name='canceled'),
              ]
