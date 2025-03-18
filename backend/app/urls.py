from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('api/create-dummy-user/', views.create_dummy_user, name='create_dummy_user'),
    path('api/create-user-ID/', views.create_user_ID, name='create_user_ID'),
    path('api/delete-user-ID/', views.delete_user_ID, name='delete_user_ID'),
    path('api/delete-latest-user/', views.delete_latest_user, name='delete_latest_user'),
    path('api/delete-all-user/', views.delete_all_user, name='delete_all_user'),
    path('api/update-user-ID/', views.update_user_ID, name='update_user_ID'),

]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()