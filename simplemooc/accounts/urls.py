from django.contrib import admin
from django.contrib.auth import views as authviews
from django.urls import include, path
from simplemooc.accounts import views

app_name = 'accounts'

urlpatterns = [
	path('entrar/', authviews.login, {'template_name':'accounts/login.html'}, name='login'),
	#path('<int:pk>', views.CourseDetails, name='CourseDetails'),
	#path('<slug:slug>', views.CourseDetails, name='CourseDetails'),
]