import xadmin

from apps.organizations.models import City, CouresOrg, Teacher


class CityAdmin(object):
    list_display = ['id', 'name', 'desc', 'add_time', ]
    # 搜索字段
    search_fields = ['name', 'desc', ]
    # 过滤器字段
    list_filter = ['name', 'add_time', ]
    # 列表页修改
    list_editable = ['name', 'desc']


class CouresOrgAdmin(object):
    list_display = ['id', 'name', 'desc', 'tag', 'city']
    # 搜索字段
    search_fields = ['name', 'desc', 'tag', 'city']
    # 过滤器字段
    list_filter = ['click_nums', 'fav_nums', 'city', 'course_nums']
    # 列表页修改
    list_editable = ['name', 'desc']


class TeacherAdmin(object):
    # 显示字段
    list_display = ['id', 'name', 'org', 'work_years', 'work_company', 'work_position', 'points']
    # 搜索字段
    search_fields = ['name', 'org', 'work_company', 'work_position', 'points']
    # 过滤器字段
    list_filter = ['work_years', 'click_nums', 'age']
    # 列表页修改
    # list_editable = ['id', 'user', 'fav_id', 'fav_type']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CouresOrg, CouresOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
