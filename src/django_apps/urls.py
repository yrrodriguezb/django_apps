from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.core.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls', namespace='books')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)