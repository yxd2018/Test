#coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Home1(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    time = models.DateField(verbose_name='时间',)
    author = models.CharField(max_length=64, verbose_name='作者')
    img = models.ImageField(upload_to='pic', verbose_name='照片')
    description = RichTextUploadingField(verbose_name='描述')

class Aboutus1(models.Model):
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    description = RichTextUploadingField(verbose_name='描述')

class Aboutus2(models.Model):
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    description = RichTextUploadingField(verbose_name='描述')

class Scenic1(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    img = models.ImageField(upload_to='pic', verbose_name='照片')

class Scenic2(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    img = models.ImageField(upload_to='pic', verbose_name='照片')

class Scenic3(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    img = models.ImageField(upload_to='pic', verbose_name='照片')

class Industries(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    author = models.CharField(max_length=64, verbose_name='作者')
    time = models.DateField(verbose_name='时间', )
    description = RichTextUploadingField(verbose_name='描述')