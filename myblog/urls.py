from django.urls import path, include
from .views import MainView, PostDetailView, SignUpView, SignInView
from . import views

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', views.logout_view, name='logout')
]


