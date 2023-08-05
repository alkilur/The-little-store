
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import Product, ProductCategory
from .views import ProductsView


class IndexViewTestCase(TestCase):
    def test_index(self):
        path = reverse('index')
        response = self.client.get(path)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products(self):
        path = reverse('products:index')
        response = self.client.get(path)
        products = Product.objects.all()[0:ProductsView.paginate_by]
        self._common_tests(response)
        self.assertEqual(list(response.context_data['products']), list(products))

    def test_products_category(self):
        products = Product.objects.all()
        category = ProductCategory.objects.first()
        path = reverse('products:category', args=(category.id,))
        response = self.client.get(path)
        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['products']),
            list(products.filter(category_id=category.id)[0:ProductsView.paginate_by])
        )
