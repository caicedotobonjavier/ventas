from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    TECNICO = '1'
    TECNOLOGO = '2'
    PROFESIONAL = '3'
    ESPECILISTA = '4'
    VENDEDOR = '5'
    ADMINISTRADOR = '6'
    OTRO = '7'

    CHOICES_OCUPACION = (
        (TECNICO, 'Tecnico'),
        (TECNOLOGO, 'Tecnologo'),
        (PROFESIONAL, 'Profesional'),
        (ESPECILISTA, 'Especilista'),
        (VENDEDOR, 'Vendedor'),
        (ADMINISTRADOR, 'Administrador'),
        (OTRO, 'Otro'),
    )
    
    email = models.EmailField('Email', max_length=254, unique=True)
    nombre_completo = models.CharField('Nombre Completo', max_length=50)
    ocupacion = models.CharField('Ocupacion', max_length=1, choices=CHOICES_OCUPACION, blank=True)
    fecha_nacimiento = models.DateField('Fehca de Nacimiento', blank=True, null=True)
    foto = models.ImageField('Foto', upload_to='Usuarios', blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=50, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_completo']

    objects = UserManager()


    def get_nombre_completo(self):
        return self.nombre_completo
    
    def get_email(self):
        return self.email

    def get_ocupacion(self):
        return self.ocupacion
