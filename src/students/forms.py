from django import forms
from .models import StudentInfo

# class StudentCreateForm(forms.Form):
# 	name   		= forms.CharField()
# 	reg_no 		= forms.CharField(required = False)
# 	cgpa		= forms.CharField(required = False)
	

class StudentAddNew(forms.ModelForm):
	class Meta:
		model = StudentInfo
		fields = [
			'name',
			'reg_no',
			'cgpa',
		]