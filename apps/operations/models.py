from django.db import models
from django.contrib.auth import get_user_model
from apps.users.models import BaseModel
from apps.courses.models import Course, CourseResource, Teacher

UserProfile = get_user_model()


# Create your models here.
class UserAsk(BaseModel):
    name = models.CharField(verbose_name="姓名", max_length=20)
    mobile = models.CharField(verbose_name="手机", max_length=11)
    course_name = models.CharField(verbose_name="课程名", max_length=50)

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{mobile}".format(name=self.name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name="评论内容")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name="数据ID")
    fav_type = models.IntegerField(default=1, verbose_name="收藏类型", choices=((1, "课程"), (2, "机构"), (3, "老师")))

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessge(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name
