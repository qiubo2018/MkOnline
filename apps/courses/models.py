from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher


# Create your models here.


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, verbose_name="老师", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="课程名称", default="", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    degree = models.CharField(verbose_name="难度", choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    category = models.CharField(verbose_name="课程类别", max_length=20, default="后端开发")
    tag = models.CharField(default="", max_length=20, verbose_name="课程标签")
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    teacher_all = models.CharField(default="", max_length=300, verbose_name="老师告诉你")
    detail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(upload_to="coureses/%y/%m", verbose_name="封面图", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"章节名称", max_length=100)
    learn_times = models.ImageField(default=0, verbose_name="学习时长（分钟数）")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    names = models.CharField(max_length=100, verbose_name="视频名称")
    learn_times = models.ImageField(default=0, verbose_name="学习时长（分钟数）")
    url = models.CharField(max_length=200, verbose_name=u"访问地址")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.names


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name="课程资源", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    file = models.FileField(upload_to="coures/resourse%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# course = Course()
