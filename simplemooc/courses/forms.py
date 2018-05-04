from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_mail_template

class ContactCourse(forms.Form):

	name = forms.CharField(label='Nome',max_length=100)
	email = forms.EmailField(label='Email')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)

	def sendMail(self, course):
		subject = 'Contato sobre o curso %s ' % course
		context = {
			'name':self.cleaned_data['name'],
			'email':self.cleaned_data['email'],
			'message':self.cleaned_data['message']
		}

		template_name = 'cursos/email_template.html'

		send_mail_template(

			subject,
			template_name,
			context,
			[settings.CONTACT_EMAIL]

		)