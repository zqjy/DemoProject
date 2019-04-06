from django.conf.urls import url, include
from rest.views import GoodListView, GoodListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'list', GoodListViewSet, base_name='list')

# 别router方式替换
# list = GoodListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    # url(r'^list[/]?', GoodListView.as_view(), name='list'),  # View方式
    # url(r'^list[/]?', list, name='list'),  # ViewSet 方式
    url(r'^', include(router.urls)),  # Router 方式
]
