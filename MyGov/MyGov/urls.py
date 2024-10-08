from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("services.urls")),
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
]