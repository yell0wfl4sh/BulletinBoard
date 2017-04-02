from django.conf.urls import url

from . import views

app_name= 'bulletin'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notices/$', views.notice, name='notices'),
    url(r'^notices/(?P<notice_id>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'^students/$', views.student, name='students'),
    url(r'^students/(?P<student_id>[0-9]+)/$', views.student_detail, name='student_detail'),
    url(r'^categories/$', views.category, name='categories'),
] 


