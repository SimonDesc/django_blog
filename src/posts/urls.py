from django.urls import path
from .views import BlogHome, BlogCreate, BlogUpdate, BlogDetail, BlogDelete
from django.contrib.auth.decorators import login_required

app_name = "posts"

urlpatterns = [
   path('', BlogHome.as_view(), name='home'),
   path('create/', login_required(BlogCreate.as_view()), name='create'),
   path('edit/<str:slug>/', login_required(BlogUpdate.as_view()), name='edit'),
   path('delete/<str:slug>/', login_required(BlogDelete.as_view()), name='delete'),
   path('<str:slug>/', login_required(BlogDetail.as_view()), name='detail'),
]