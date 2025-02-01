from django.urls import path, include

urlpatterns = [
    path('blog/', include(('devopsdjango.blog.urls', 'blog'))),
]
