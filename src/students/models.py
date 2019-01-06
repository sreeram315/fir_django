from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from time import sleep

from .utils import unique_slug_generator
from .validator import validate_name

# Create your models here.

User = settings.AUTH_USER_MODEL

class StudentInfo(models.Model):
	owner		= models.ForeignKey(User, on_delete=models.CASCADE) # class_instance.model_set.all()
	name   		= models.CharField(max_length = 120, null = False, blank = False, validators = [validate_name])
	reg_no 		= models.CharField(max_length = 20, null  = True, blank = True)
	cgpa		= models.CharField(max_length = 10, null = True, blank = True)
	timestamp	= models.DateTimeField(auto_now_add = True)
	slug  		= models.SlugField(null = True, blank = True)

	def get_absolute_url(self):
		return reverse('students:search', kwargs = {'slug': self.slug})

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

pre_save.connect(rl_pre_save_receiver, sender = StudentInfo)

post_save.connect(rl_post_save_receiver, sender = StudentInfo)	
