from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import LoginView
# from django.contrib.auth.views import LoginView
import random

# from .forms import  StudentAddNew#, StudentCreateForm
from .models import TeacherInfo
from .forms import TeacherAddNew

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
		return render(request, 'teachers_templates/teacher_home.html', replacements)

class TeacherListView(ListView):
	models 				=   TeacherInfo
	context_object_name =  'obj_list'
	queryset 			= 	TeacherInfo.objects.all()
	template_name 		=  'teachers_templates/teacher_show.html'

class TeacherSearch(ListView):
	def get_queryset(self):
		queryset = TeacherInfo.objects.filter(slug = self.kwargs['slug'])
		return queryset
	context_object_name 	 =  'obj_list'
	template_name			 =  'teachers_templates/teacher_show.html'

class TeacherNewForm(LoginRequiredMixin, CreateView):
	login_url 		= 		'/login/'
	form_class 		= 		TeacherAddNew
	template_name 	= 		'teachers_templates/add_teacher_form.html'
	#success_url 	=		'teachers/teacher-list/'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.owner = self.request.user
		return super(TeacherNewForm, self).form_valid(form)
