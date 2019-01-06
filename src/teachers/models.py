from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .validator import validate_name
from django.urls import reverse
import datetime

User = settings.AUTH_USER_MODEL
from students.models import StudentInfo
from .utils import unique_slug_generator

class TeacherInfo(models.Model):
	#assosiations
	owner 			=	models.ForeignKey(User, on_delete = models.CASCADE, default =2)
	student 		=	models.ForeignKey(StudentInfo, on_delete = models.CASCADE, default = 3)
	#items
	name 			=	models.CharField(max_length = 120, null = False, blank = False, validators = [validate_name])
	uid				=	models.CharField(max_length = 20, null = False, blank = False,  default = 'NOT PROVIDED')
	department		=	models.CharField(max_length = 50, null = True, blank = True, default = 'NOT PROVIDED')
	description		=	models.TextField(null = True, blank = True, default = 'NOT PROVIDED')
	slug  			= 	models.SlugField(null = True, blank = True)
	timestamp		= 	models.DateTimeField(auto_now_add = True)#, default = timezone.now)


	def get_absolute_url(self):
		return reverse('teachers:search', kwargs = {'slug': self.slug})

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	instance.name = instance.name.title()
	print('Saving...')
	print(instance.timestamp)


def rl_post_save_receiver(sender, instance, *args, **kwargs):
	print('Saving...')
	print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender = TeacherInfo)

post_save.connect(rl_post_save_receiver, sender = TeacherInfo)







