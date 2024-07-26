#
from django.db import models

class ProductoManager(models.Manager):
    
    def productos_x_marcas(self, id):
        consulta = self.filter(
            marca__id = id
        )
        
        return consulta