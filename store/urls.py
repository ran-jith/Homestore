
from django.conf.urls import url,include
from django.contrib import admin
from.import views                      #"from." means from current directory and need to import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from store import views as store_views #there a 2 views present here thats why


app_name = 'store'

urlpatterns = [
    url(r'^$',views.product_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$',views.product_detail, name="detail"),

]
