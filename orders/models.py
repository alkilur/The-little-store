
from django.db import models

from products.models import BasketItem
from users.models import User


class Order(models.Model):

    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=256, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    basket_history = models.JSONField(default=dict)
    status = models.PositiveSmallIntegerField(default=CREATED, choices=STATUSES)

    def __str__(self):
        return f'Заказ #{self.id}. {self.first_name} {self.last_name}'


    def update_after_payment(self):
        basket_items = BasketItem.objects.filter(user=self.initiator)
        self.basket_history = {
            'purchased_items': [item.de_json() for item in basket_items],
            'total_sum': float(basket_items.total_sum())
        }
        basket_items.delete()
        self.status = self.PAID
        self.save()
