from django.contrib import admin
from django.urls import path, include, re_path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solutions/', include('solutions.urls')),
    path('about/', views.about),
    path('filtered_solutions/<str:tipos>/', views.solution_filtered, name='filtered_solutions'),
    path('',views.homepage, name='my_homepage')
]

urlpatterns += staticfiles_urlpatterns()


