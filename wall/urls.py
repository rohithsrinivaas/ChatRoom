from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^users/(?P<user_name>[\w\-]+)/$', views.user_wall, name='user_wall'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signUpHandler/$',views.signUpHandler,name = 'signUpHandler'),
    url(r'^logInHandler/$',views.logInHandler,name ='logInHandler'),
    url(r'^logout/$',views.logout,name ='logout')
]
