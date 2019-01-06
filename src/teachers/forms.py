from django import forms
from .models import TeacherInfo

# class StudentCreateForm(forms.Form):
# 	name   		= forms.CharField()
# 	reg_no 		= forms.CharField(required = False)
# 	cgpa		= forms.CharField(required = False)
	

class TeacherAddNew(forms.ModelForm):
	class Meta:
		model = TeacherInfo
		fields = [
			'name',
			'uid',
			'department',
			'description',
		]