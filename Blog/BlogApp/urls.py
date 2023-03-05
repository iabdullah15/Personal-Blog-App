from django.urls import path
from . import views


urlpatterns = [
    # path('', views.test),
    path('', views.Home.as_view(), name='home'),
    path('blog', views.BlogPosts.as_view(), name='blog'),
]