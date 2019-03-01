from django.db import models
from django.core import validators


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    """ファイルのアップロード"""
    # thumbnial = models.FileField(upload_to='files/%Y/%m/%d', validators=[
        #拡張子の検証
    #     validators.FileExtensionValidator(['txt'], message="拡張子はtxtのみ")
    # ])
    
    """画像のアップロード"""
    thumbnail = models.ImageField(upload_to="%Y/%m/%d")