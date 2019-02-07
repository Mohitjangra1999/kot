"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views
app_name = 'books'
urlpatterns = [
    url(r'^$', views.first_page.as_view(), name='first_page'),
    url(r'^books/$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.UserFormView.as_view(), name='signup'),
    url(r'^login/$', views.login_user.as_view(), name='login'),
    url(r'^login/check/$', views.checklogin.as_view(), name='login_check'),
    url(r'^log_out/$', views.log_out.as_view(), name='log_out'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.BookCreate.as_view(), name='book_add'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
    url(r'^delete/success_page/$', views.Delete_Success_page.as_view(),name='delete_success'),
]
