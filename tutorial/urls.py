from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from quickstart.views import (
                    UserViewSet, 
                    GroupViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]

