from django.contrib import admin
from django.urls import path , include
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/',views.deshboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('articles/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
   

   
]
