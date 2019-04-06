from django.db import models

# Create your models here.
class PicModel(models.Model):
    """
    上传图片模型类
    """
    image = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'd_pic_model'
        verbose_name = '上传图片'
        verbose_name_plural = verbose_name
