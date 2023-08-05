
from .models import BasketItem


def basket_items(request):
    user = request.user
    return {'basket_items': BasketItem.objects.filter(user=user)
            if user.is_authenticated else []}
