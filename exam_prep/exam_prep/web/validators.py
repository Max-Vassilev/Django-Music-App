from django.core.exceptions import ValidationError


def alpha_num(value):
    for ch in value:
        if not (ch.isalnum() or ch == "_"):
            raise ValidationError("Ensure this value contains only letters,numbers, and underscore.")
