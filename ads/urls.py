from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ads import views


app_name = 'ads'

urlpatterns = [

    path('catalog/', views.catalog_view, name='catalog'),
    path('catalog/<int:page>/', views.catalog_view, name='catalog'),
    path('create_ad/', views.create_ad, name='create_ad'),
    path('catalog/id-<int:ad_id>/', views.ad_detail_view, name='ad_detail'),
    path('delete_ad/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('update_ad/<int:ad_id>/', views.update_ad, name='update_ad'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    #path('search/', views.CatalogView.as_view(), name='search'),
    #path('catalog/', views.catalog_view, name='catalog'),
 #path('catalog/<slug:detail_slug>/', views.ad_detail_view, name='ad_detail'),