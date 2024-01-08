from  .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name=''),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create-record'),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name='record'),

    path('delete/<int:pk>', views.delete_record, name='delete'),
]
