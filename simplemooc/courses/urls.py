from django.contrib import admin
from django.urls import include, path
from simplemooc.courses import views

app_name = 'courses'

urlpatterns = [
	path('', views.index, name='index'),
	#path('<int:pk>', views.CourseDetails, name='CourseDetails'),
	path('<slug:slug>', views.CourseDetails, name='CourseDetails'),
]