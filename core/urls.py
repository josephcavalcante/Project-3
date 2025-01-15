from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI

api = NinjaAPI()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]