from django.conf.urls import url, include
from .views import FirstAppView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'first-app', FirstAppView)


urlpatterns = [
    url(r'api/', include(router.urls))
]
