import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = "在线教学后台管理"
    site_footer = "在线教学"
    # 菜单收缩
    menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CouresAdmin(object):
    list_display = ['id', 'name', 'teacher', 'desc', 'detail', 'degree', 'category', 'learn_times', 'students', ]
    search_fields = ['name', 'desc', 'detail', 'degree', 'category', 'students']
    # 过滤器字段
    list_filter = ['learn_times', 'name', 'desc', 'teacher__name']
    # 列表页修改
    list_editable = ['name', 'desc', 'degree']


class LessonAdmin(object):
    list_display = ['id', 'course', 'learn_times', ]
    search_fields = ['course']
    # 过滤器字段
    list_filter = ['learn_times', 'course', "course__name"]
    # 列表页修改
    list_editable = ['course']


class VideoAdmin(object):
    list_display = ['id', 'names', 'learn_times', 'lesson']
    search_fields = ['names', 'lesson']
    # 过滤器字段
    list_filter = ['learn_times', 'names', 'lesson']
    # 列表页修改
    list_editable = ['names']


class CourseResourceAdmin(object):
    list_display = ['id', 'name', 'file']
    search_fields = ['name', 'file']
    # 过滤器字段
    list_filter = ['name', 'file']
    # 列表页修改
    list_editable = ['name']


xadmin.site.register(Course, CouresAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
# 设置头部和底部
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
# 设置风格
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
