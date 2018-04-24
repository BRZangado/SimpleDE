from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from simplemooc.courses.models import Course

def index(request):
	courses = Course.objects.all()
	template_name = 'cursos/cursos.html'
	context = {
		'courses':courses
	}
	return render(request, template_name, context)

def CourseDetails(request, slug):
	course = get_object_or_404(Course, slug=slug)
	context = {
		'course':course
	}
	template_name = 'cursos/detalhes.html'
	return render(request, template_name, context)