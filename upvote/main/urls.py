from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('',views.UpVotePageView.as_view(),name='upvote'),  
]
