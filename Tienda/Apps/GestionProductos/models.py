from django.db import models

# Create your models here.

class Producto(models.Model):
    NombreProducto = models.CharField(max_length=30)
    DescripcionProducto = models.CharField(max_length=30)
    ClaveProducto = models.CharField(max_length=5)
    PrecioProducto = models.CharField(max_length=10)
    FechaRegistro = models.DateField()

    def __str__(self):
        return "{0} ({1}) ({2}) ({3})".format(self.NombreProducto, self.DescripcionProducto, self.ClaveProducto, self.PrecioProducto)
    
    
class Estante(models.Model):
    NombreEstante=models.CharField(max_length=30)
    Capacidad=models.PositiveBigIntegerField()
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.NombreEstante, self.Capacidad)


class Registro(models.Model):
    Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    Estante = models.ForeignKey(Estante, null=False, blank=False, on_delete=models.CASCADE)
    FechaRegistro= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Producto, self.Estante.NombreEstante)