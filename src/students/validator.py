from django.core.exceptions import ValidationError

def validate_name(value):
	if len(value) <= 2:
		raise ValidationError('This is not a valid name')