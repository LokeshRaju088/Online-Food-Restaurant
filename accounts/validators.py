from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] #cover_image.jpg
    valid_extensions = ['.png','.jpg','.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('unsupported file extension. Allowed only : '+ str(valid_extensions))