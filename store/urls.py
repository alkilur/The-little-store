
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token

from orders.views import stripe_webhook_view
from products.views import IndexView

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns = [
                path('', include(static_urlpatterns)),
                path('', IndexView.as_view(), name='index'),
                path('admin/', admin.site.urls),
                path('accounts/', include('allauth.urls')),
                path('products/', include('products.urls', namespace='products')),
                path('users/', include('users.urls', namespace='users')),
                path('orders/', include('orders.urls', namespace='orders')),
                path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),

                path('api/', include('api.urls', namespace='api')),
                path('api-token-auth/', obtain_auth_token),
              ]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
