# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.TextField(max_length=255, null=True, blank=True)
    celular = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clientes(models.Model):

    #__Clientes_FIELDS__
    nombre = models.TextField(max_length=255, null=True, blank=True)
    direccion = models.TextField(max_length=255, null=True, blank=True)

    #__Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Clientes")
        verbose_name_plural = _("Clientes")


class Producto(models.Model):

    #__Producto_FIELDS__
    tipo = models.TextField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    #__Producto_FIELDS__END

    class Meta:
        verbose_name        = _("Producto")
        verbose_name_plural = _("Producto")


class Cotizacion(models.Model):

    #__Cotizacion_FIELDS__
    contacto = models.TextField(max_length=255, null=True, blank=True)

    #__Cotizacion_FIELDS__END

    class Meta:
        verbose_name        = _("Cotizacion")
        verbose_name_plural = _("Cotizacion")


class Detalles_Cotizacion(models.Model):

    #__Detalles_Cotizacion_FIELDS__
    precio_unitario = models.TextField(max_length=255, null=True, blank=True)

    #__Detalles_Cotizacion_FIELDS__END

    class Meta:
        verbose_name        = _("Detalles_Cotizacion")
        verbose_name_plural = _("Detalles_Cotizacion")



#__MODELS__END
