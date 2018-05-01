from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactCourse(forms.Form):

	name = forms.CharField(label='Nome',max_length=100)
	email = forms.EmailField(label='Email')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)

	def sendMail(self, course):
		subject = 'Contato sobre o curso %s ' % course
		message = 'Nome: %(name)s; \nEmail: %(email)s; \n%(message)s'
		context = {
			'name':self.cleaned_data['name'],
			'email':self.cleaned_data['email'],
			'message':self.cleaned_data['message']
		}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
