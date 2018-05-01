from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from simplemooc.courses.models import Course
from simplemooc.courses.forms import ContactCourse

def index(request):
	courses = Course.objects.all()
	template_name = 'cursos/cursos.html'
	context = {
		'courses':courses
	}
	return render(request, template_name, context)

def CourseDetails(request, slug):
	course = get_object_or_404(Course, slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.sendMail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()
		
	context['course'] = course
	context['form'] = form
	template_name = 'cursos/detalhes.html'
	return render(request, template_name, context)