from django.urls import path
from . import views


urlpatterns = [
    #path('/', views.user_form, name='user_form'), 
    path('/', views.user_list, name='user_list'),
    path(
        'users/edit/<int:id>/',
        views.user_update,
        name='user_update'
    ),

    path(
        'users/delete/<int:id>/',
        views.user_delete,
        name='user_delete'
    ),
]