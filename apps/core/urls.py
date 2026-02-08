from django.urls import path
from .views import input_view,result_view,reset_session


urlpatterns = [
        path('',input_view,name="home"),
        path('result',result_view,name="result"),
        path("reset/", reset_session, name="reset"),
    ]