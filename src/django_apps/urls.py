from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from apps.blog.sitemaps import PostSitemap
from apps.core.views import HomeView


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls', namespace='books')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)