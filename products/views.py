
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import BasketItem, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    BasketItem.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, item_id):
    item = BasketItem.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# @login_required
# def basket_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     basket_item = BasketItem.objects.filter(user=request.user, product=product).first()

#     if basket_item:
#         basket_item.quantity += 1
#         basket_item.save()
#     else:
#         BasketItem.objects.create(user=request.user, product=product, quantity=1)

#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
