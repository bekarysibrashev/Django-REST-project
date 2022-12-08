from django.urls import path, include
from .views import MainView, PostDetailView, SignUpView, SignInView, LogOutView, FeedbackView, SuccessView,PostCreateView, SearchView
from . import views

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<slug>', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('contactus/', FeedbackView.as_view(), name='contactus'),
    path('contactus/success', SuccessView.as_view(), name='success'),
    path('search/', SearchView.as_view(), name='search')

   
]


