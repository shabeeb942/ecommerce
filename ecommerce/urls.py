from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("products.urls", namespace="products")),
        path("web", include("web.urls", namespace="web")),
        path("main", include("main.urls", namespace="main")),
        path("orders", include("orders.urls", namespace="orders")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)