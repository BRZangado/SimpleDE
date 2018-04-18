from django.shortcuts import render
from django.http import HttpResponse
from simplemooc.courses.models import Course

def index(request):
	courses = Course.objects.all()
	template_name = 'cursos/cursos.html'
	context = {
		'courses':courses
	}
	return render(request, template_name, context)