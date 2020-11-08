from django.db import models


# Create your models here.
class Users(models.Model):
    SEX_ITEMS = (
        (2, '未知'),
        (1, '男'),
        (0, '女'),
    )
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, default=2, verbose_name='性别')
    idcard = models.CharField(max_length=18, verbose_name='身份证号码', unique=True)
    email = models.EmailField(verbose_name='邮箱地址')
    address = models.CharField(max_length=256, verbose_name='家庭住址')
    company = models.CharField(max_length=256, verbose_name='所属公司')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '用户管理'
