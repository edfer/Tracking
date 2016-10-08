from django.contrib.auth.models import User
from django.db import models

# Create your models here.

LICENSE_COPYRIGHT = 'RIG'
LICENSE_COPYLEFT = 'LEF'
LICENSE_CC = 'CC'


LICENSES = (
     (LICENSE_COPYRIGHT, 'Copyright'),
     (LICENSE_COPYLEFT, 'Copyleft'),
     (LICENSE_CC, 'Creative Commons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY =(
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)

class Photo(models.Model):


    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    license = models.CharField(max_length=3, choices=LICENSES, default=LICENSE_CC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    # Definimos el nombre del modelo de la app!
    # el nombre que se ve en el admin cuando entramos en el modelo registrado en admin.py

    def __str__(self):
        return self.name