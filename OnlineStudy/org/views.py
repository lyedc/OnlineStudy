from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage

from .models import CityDict, CourseOrg


# Create your views here.

class OrgListView(View):
    """课程机构列表页面"""

    def get(self, request, *args, **kwargs):  # 返回的是字串类型的  使用不定长字典的方式
        ordering = request.GET.get('ordering', '-click_nums')
        current_page = request.GET.get('page', '1')
        city_list = CityDict.objects.all()
        condition = {}
        for key, value in kwargs.items():
            if value == '0':
                pass  # 除去当传递的参数是0 的情况  0 传递到数据库过滤中是控制 不符合要求 过滤掉
            else:
                condition[key] = value
        course_org_list = CourseOrg.objects.filter(**condition).order_by(ordering)
        course_org_ordering = CourseOrg.objects.all().order_by('-students')[:3]  # 授课机构的排名
        nav_url = 'org_list'  # 控制导航变色的变量
        current_page_course, page_rang = self.get_page(course_org_list, current_page)
        return render(request, 'org/org-list.html', locals())

    def get_page(self, course_org_list, current_page):
        # 分页的开始
        paginator = Paginator(course_org_list, 1)
        try:
            current_page_course = paginator.page(int(current_page))
        except (InvalidPage, PageNotAnInteger, EmptyPage):
            current_page_course = paginator.page(1)
        page_rang = paginator.page_range  # 获取总的页数
        return current_page_course, page_rang


class OrgStudyView(View):
    """学习咨询视图"""

    def post(self, request):
        if request.is_ajax():
            if request.method == "POST":
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                course_name = request.POST.get('course_name')
                print("上交的ajax 数据是", name)
                print("上交的ajax 数据是", mobile)
                print("上交的ajax 数据是", course_name)
                result = {'code': 1, 'err': 'null'}
                return JsonResponse(result)


class OrgDetailView(View):
    """机构详情页面"""
    def get(self, request, nid):
        course_org_detail = CourseOrg.objects.filter(id=int(nid)).first()
        return render(request, 'org/org-detail-homepage.html', locals())
