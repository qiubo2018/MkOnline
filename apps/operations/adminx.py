import xadmin

from apps.operations.models import UserAsk, UserMessge, UserCourse, UserFavorite, CourseComments


class UserAskAdmin(object):
    list_display = ['id', 'name', 'mobile', 'course_name', ]
    # 搜索字段
    search_fields = ['id', 'name', 'mobile', 'course_name', ]
    # 过滤器字段
    list_filter = ['name', 'mobile']
    # 列表页修改
    list_editable = ['name', 'mobile', 'course_name', ]


class UserCourseAdmin(object):
    list_display = ['id', 'user', 'course', ]
    # 搜索字段
    search_fields = ['user', 'course', ]
    # 过滤器字段
    list_filter = ['user', 'course']
    # 列表页修改


class UserFavoriteAdmin(object):
    # 显示字段
    list_display = ['id', 'user', 'fav_id', 'fav_type']
    # 搜索字段
    search_fields = ['user', 'fav_id', 'fav_type']
    # 过滤器字段
    list_filter = ['user', 'fav_id', 'fav_type']
    # 列表页修改
    # list_editable = ['id', 'user', 'fav_id', 'fav_type']


class UserMessgeAdmin(object):
    # 显示字段
    list_display = ['id', 'user', 'message', 'has_read']
    # 搜索字段
    search_fields = ['user', 'message']
    # 过滤器字段
    list_filter = ['user', 'message', 'has_read']
    # 列表页修改
    # list_editable = ['id', 'user', 'fav_id', 'fav_type']


class CourseCommentsAdmin(object):
    # 显示字段
    list_display = ['id', 'user', 'course', 'comments']
    # 搜索字段
    search_fields = ['user', 'course', 'comments']
    # 过滤器字段
    list_filter = ['user', 'course']
    # 列表页修改
    # list_editable = ['id', 'user', 'fav_id', 'fav_type']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessge, UserMessgeAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
