from django.urls import path,include
from basicapp import views
#As we are using relative template calling

app_name='basicapp'
urlpatterns=[
path('register/',views.register,name='register'),
# path('',vi,)
path('user_login/',views.user_login,name='user_login'),
]
