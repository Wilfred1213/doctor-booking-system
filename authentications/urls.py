from django.urls import path
from authentications.views import signup, login_view, signout

app_name ='authentications'
urlpatterns = [
   
    path('signup/', signup, name = 'signup'),
    path('login_view/', login_view, name = 'login_view'),
    path('signout/', signout, name = 'signout'),
    

] 