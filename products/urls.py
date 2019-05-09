from django.conf.urls import url,include

from . import views
urlpatterns = [
    url(r'^product_list/', views.productlistview, name ='product_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.productdetailview ,name = 'product-detail'),
    url(r'^form/', views.productaddview ,name = 'form'),
    url(r'^success/', views.successview ,name = 'success'),

]
