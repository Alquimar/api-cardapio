from django.contrib import admin
from django.urls import path, include
from estabelecimento.views import EstabelecimentosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estabelecimentos', EstabelecimentosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
