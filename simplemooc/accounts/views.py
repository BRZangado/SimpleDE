from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
	template_name = 'accounts/register.html'

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()

	context = {
		'form': form
	}
	return render(request, template_name, context)
