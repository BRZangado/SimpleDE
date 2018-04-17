from django.contrib import admin
from django.urls import include, path
from simplemooc.core import views
from simplemooc.courses import views as viewsCurso

app_name = 'core'

urlpatterns = [
	path('', views.home, name='home'),
	path('contato/', views.contact, name='contact'),
]