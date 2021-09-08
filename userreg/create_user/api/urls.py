from django.urls import path
from create_user.api.views import registration_view,Viewhello_view

app_name='create_user'

urlpatterns=[
    path('register',registration_view,name="register"),
    path('view',Viewhello_view,name="view")
]