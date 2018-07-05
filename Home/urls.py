from django.conf.urls import url,include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^store/', include('store.urls')),
    #url(r'^accounts/',include('accounts.urls')),
    url(r'^about/$', views.about),
    url(r'^home/$', views.homepage),
]
