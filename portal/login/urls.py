from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LoginIndex.as_view(), name='loginIndex'),
    url(r'^home/', views.HomePage.as_view(), name='homePage'),
]