from django.conf.urls import url
from apps.upload.views import UploadView

urlpatterns = [
    url(r'^pic/', UploadView.as_view(), name='pic'),
]
