from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import CategoryListView,CategoryDetailView

urlpatterns = [
    # Examples:
    url(r'^$', CategoryListView.as_view(), name='categories'),   
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),   
    #url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),   
]  