from django.urls import path
from register import views
app_name = "reg"

urlpatterns=[
    path("register/",views.register,name="register"),
    path("logout/",views.logout,name="logout"),
    path("index/<input>/",views.index,name="index"),
]
