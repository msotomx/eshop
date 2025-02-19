from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

# class Proveedor(models.Model):
#    rfc = models.CharField(max_length=13,default='')
#    nombre = models.CharField(max_length=50)
#    contacto_compras = models.CharField(max_length=50)
#    email_compras = models.EmailField(max_length=40)
#    cel_compras = models.CharField(max_length=12)
#    contacto_pagos = models.CharField(max_length=50)
#    email_pagos = models.EmailField(max_length=40)
#    cel_pagos = models.CharField(max_length=12)
#    contacto_almacen = models.CharField(max_length=50)
#    email_almacen = models.EmailField(max_length=40)
#    cel_almacen = models.CharField(max_length=12)
#    contacto_otro = models.CharField(max_length=50)
#    email_otro = models.EmailField(max_length=40)
#    cel_otro = models.CharField(max_length=12)
#    telefono = models.CharField(max_length=12)
#    calle = models.CharField(max_length=50)
#    colonia = models.CharField(max_length=50)
#    ciudad = models.CharField(max_length=50)
#    estado = models.CharField(max_length=3)
#    pais = models.CharField(max_length=20)
#    plazo_credito = models.SmallIntegerField(default=0)
#    comentarios = models.TextField(null=True)
#
#    def __str__(self):
#        return self.nombre

class Producto(models.Model):
#    codigo = models.CharField(max_length=20, primary_key=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)
#    sku = models.CharField(max_length=12, default='')
#    marca = models.CharField(max_length=30)
#    proveedor = models.ForeignKey(Proveedor,on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

#class Clientes(models.Model):
#    nombre = models.CharField(max_length=200)
#    fecha_registro = models.DateTimeField(auto_now_add=True)
#    campo_libre = models.CharField(max_length=20)
#
#    def __str__(self):
#        return self.nombre
