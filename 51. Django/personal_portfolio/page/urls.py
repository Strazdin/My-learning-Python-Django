from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.page, name='page'),
    path('<int:page_id>/', views.more, name='more'),
]