from django.urls import path
from . import views
from .views import PersonUpdateView, PersonCreateView

urlpatterns = [
    path('', views.home, name='people'),
    path('add/<pk>',views.add_email_and_phone, name='add_email_and_phone'),
    path('delete/<pk>', views.delete_user, name='delete_user'),
    path('update/<int:pk>/',PersonUpdateView.as_view(),name='update_user'),
    path('new/',PersonCreateView.as_view(),name='create_user'),


]