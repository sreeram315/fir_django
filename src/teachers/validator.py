from django.core.exceptions import ValidationError


def validate_name(value):
	if len(value) < 3:
		raise ValidationError('Not a valid name')