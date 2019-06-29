"""dprojx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
    #path('admin/', admin.site.urls),
#]

"""
from django.conf.urls import url
from dappx import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_Login,name='user_login'),
]


from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from dappx import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    #url(r'^dappx/',include('dappx.urls')),
    url(r'^logout/$', views.user_Logout, name='logout'),
] """


from django.contrib import admin
from django.urls import path
from dappx.views import register,special,user_Login,user_Logout,index,signin,looks,admin1,feedback

urlpatterns=[
    path('admin/',admin.site.urls),
    path('signin/',signin,name='signin'),
    #path('email/',send_email,name='email'),
    path('looks/',looks,name='looks'),
    path('register/',register,name='register'),
    path('index/',index,name='index'),
    path('special/',special,name='special'),
    path('login/',user_Login,name='login'),
    path('logout/',user_Logout,name='logout'),
    path('admin1/',admin1,name='admin1'),
    path('feedback/',feedback,name='feedback'),
]
