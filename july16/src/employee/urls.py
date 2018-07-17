from rest_framework import routers
from django.conf.urls import include, url
from views import EmployeeViewSet, ManagerViewSet


router = routers.SimpleRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'manager', ManagerViewSet)

urlpatterns = [
    url(r'api/', include(router.urls))
]
