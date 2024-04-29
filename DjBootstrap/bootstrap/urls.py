from django.urls import path

from . import views

#app_name = 'bootstrap_index'
urlpatterns = [
    #url(r'',views.bootstrap_index, name="index"),
    path("", views.bootstrap_index,name="index"),  # ไม่มีการใช้ regex

]