from django.urls import path, include
from . import views as store_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', store_views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", store_views.robots_txt),
]
