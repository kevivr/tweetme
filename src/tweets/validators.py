from django.core.exceptions import ValidationError


def validate_text(text):
    content = text
    if content == "":
        raise ValidationError("Cannot be blank")
    return text