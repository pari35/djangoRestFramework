from django import views
from django.contrib import admin
from django.urls import path
from apis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.studentAPI.a_view()),
]