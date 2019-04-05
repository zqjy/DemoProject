from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from django.conf import settings
from apps.upload.models import PicModel


# Create your views here.
# demo/upload
class UploadView(View):
    def get(self, request):
        context = {}
        return render(request, 'demo/upload.html', context)

    def post(self, request):
        # 1.获取上传文件的处理对象
        img = request.FILES['img']
        save_path = '%s/img/%s' % (settings.MEDIA_ROOT, img.name)  # 文件保存路径
        # 2.创建一个文件
        with open(save_path, 'wb') as f:
            # 3.获取上传文件的内容并写到文件中
            for content in img.chunks():
                f.write(content)
        # 4.在数据库中保存上传的数据
        PicModel.objects.create(image='img/%s' % img.name)
        # 5.返回
        return HttpResponse('OK!')

    def put(self, request):
        print('*'*20)
        return HttpResponse('OK!')

    def delete(self, request):
        pass
