from django.urls import path
from core.views import *
from . import views

app_name='core'

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('success/', success, name='success'),
    path('approve/<int:id>/', approve, name='approve'),
    path('decline/<int:id>/', decline, name='decline'),
    path('moderation/<int:id>/', moderation, name='moderation'),
    path('make_user/<int:id>/', make_user, name='make_user'),
] 