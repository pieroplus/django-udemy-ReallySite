from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from mysite import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.mypage),
    path('', views.index),
    path('blog/', include('blog.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
