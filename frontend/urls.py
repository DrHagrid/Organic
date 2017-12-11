from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page, name='start'),
    url(r'^(?P<class_text_id>\w+)/$', views.class_page, name='class')
]
