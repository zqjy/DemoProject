from django.conf.urls import url, include
from apps.users.views import SmsCodeViewset, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# 发送短信验证
router.register(r'codes', SmsCodeViewset, base_name='codes')
# 用户注册
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    url(r'^', include(router.urls)),  # Router 方式
]
