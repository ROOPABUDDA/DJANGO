from django.conf.urls import url, include
from .views import snippet_list, snippet_detail
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'^snippets/$', snippet_list)
router.register(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail)
router.register(r'suites', SuitesViewset, base_name='suites')


urlpatterns = [
    url(r'api/', include(router.urls))
]
