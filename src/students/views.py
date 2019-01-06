from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import LoginView
# from django.contrib.auth.views import LoginView
import random

from .forms import  StudentAddNew#, StudentCreateForm
from .models import StudentInfo


class HomeView(View):
	def get(self, request, *args, **kwargs):
		num = random.randint(0,1000000)
		stu_name, stu_age, stu_email = 'Sreeram Maram', '19', 'sreerammaram2@gmail.com'
		replacements = {
			'stu_name'	: stu_name,
			'stu_age'	: stu_age,
			'stu_email'	: stu_email,
			'num'		: [random.randint(0,1000000) for i in range(5)],
			'boolian'	: True,
		}
		return render(request, 'home.html', replacements)

class ContactView(TemplateView):
	template_name = 'contact_me.html'

	def get_context_data(self, *args, **kwargs):
		context = {
			'phone_number' : '8919937557',
			'email'        : 'sreerammaram2@gmail.com'
 		}
		return context

class StudentListView(ListView):
	models 				=   StudentInfo
	context_object_name =  'obj_list'
	queryset 			= 	StudentInfo.objects.all()
	template_name 		=  'students_templates/student_show.html'
	
class StudentSearch(ListView):
	def get_queryset(self):
		queryset = StudentInfo.objects.filter(slug = self.kwargs['slug'])
		return queryset
	context_object_name 	 =  'obj_list'
	template_name			 =  'students_templates/student_show.html'

class StudentNewForm(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	form_class = StudentAddNew
	template_name = 'students_templates/add_student_form.html'
	#success_url 	=	'/student-list/'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.owner = self.request.user
		return super(StudentNewForm, self).form_valid(form)















# def add_student_form(request):
# 	print('THSI IS CALLED')
# 	form = StudentCreateForm()
# 	if request.method == 'POST':
# 		form = StudentCreateForm(request.POST)
# 		if form.is_valid():
# 			obj = StudentInfo.objects.create(
# 					name = form.cleaned_data.get('name'),
# 					reg_no = form.cleaned_data.get('reg_no'),
# 					cgpa = form.cleaned_data.get('cgpa')
# 				)
# 			if form.errors:
# 				print(form.errors)
# 	return render(request, 'students_templates/add_student_form.html', {'form': form})



	

