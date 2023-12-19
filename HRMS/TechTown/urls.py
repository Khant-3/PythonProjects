from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path("emp/add/", views.emp_add, name="emp_add"),
    path("emp/list/", views.emp_list, name="emp_list"),
    path("emp/edit/<int:emp_id>/", views.emp_edit, name="emp_edit"),
    path("emp/detail/<int:emp_id>/", views.emp_detail, name="emp_detail"),
    path("emp/del/<int:emp_id>/", views.emp_delete, name="emp_delete"),
    path("dandp/list/", views.dept_and_role, name="dept_and_role"),
    path("dedit/<int:dept_id>/", views.dept_edit, name="dept_edit"),
    path("ddel/<int:dept_id>/", views.dept_del, name="dept_del"),
    path("redit/<int:role_id>/", views.role_edit, name="role_edit"),
    path("rdel/<int:role_id>/", views.role_del, name="role_del"),
    path("leaves/", views.leaves, name="leave"),
    path("leaves/approve/<int:leave_id>/", views.leave_approve, name="leave_approve"),
    path("leaves/details/<int:leave_id>/<int:leave_approval_id>/", views.leave_detail, name="leave_detail"),
    path("leaves/delete/<int:leave_id>/", views.leave_delete, name="leave_delete"),
    path("attd/del/<int:attd_id>/", views.attd_del, name="attd_del"),
    path("home/", views.home, name="home"),
    path("", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("register/", views.register, name="register"),
    re_path(r'^.*/$',views.custom_404_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
