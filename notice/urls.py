from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from notice.views import NoticeList
from notice.models import Notice
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$',NoticeList.as_view(),name= "notice-detail"),
	url(r'^notice/(?P<pk>\d+)$',DetailView.as_view(model=Notice,template_name='notice/post.html')),
	url(r'^contact',views.contact,name="contact"),
	url(r'^about',views.about,name="about"),
	]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)