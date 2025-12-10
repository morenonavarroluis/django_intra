from django.db import models
# Importar el modelo de usuario de Django de la manera estándar.
from django.contrib.auth import get_user_model 

# Obtiene el modelo de usuario activo (auth.User o un modelo custom)
User = get_user_model()


## 1. Modelos de Catálogo (Foreign Keys)

class Area(models.Model):
    """Corresponde a la tabla 'intranet area'."""
    ID_AREA = models.AutoField(primary_key=True)
    AREA = models.TextField(verbose_name="Nombre del Área")

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.AREA


class Status(models.Model):
    """Corresponde a la tabla 'intranet status'."""
    ID_STATUS = models.AutoField(primary_key=True)
    STATUS = models.TextField(verbose_name="Estado del Reporte")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados" 

    def __str__(self):
        return self.STATUS


class Level(models.Model):
    ID_LEVEL = models.AutoField(primary_key=True)
    LEVEL = models.CharField(max_length=20, verbose_name="Nivel/Prioridad")

    class Meta:
        verbose_name = "Nivel de Prioridad"
        verbose_name_plural = "Niveles de Prioridad"

    def __str__(self):
        return self.LEVEL




class Report(models.Model):
    """Corresponde a la tabla 'intranet report' (Casos/Tickets de Soporte)."""
    
    ID_REPORT = models.AutoField(primary_key=True) 
    TITLE = models.CharField(max_length=100, verbose_name="Título del Reporte")
    descripcion=models.CharField(max_length=100, verbose_name="asunto del Reporte")
    # Usuario que levanta el ticket.
    reporter_user = models.ForeignKey(
        User,  
        on_delete=models.CASCADE,
        related_name='reports_created',
        verbose_name="Usuario Reportante"
    )
    
    # Técnico asignado que gestiona el caso.
    technician_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reports_assigned',
        verbose_name="Técnico Asignado"
    )
    
    # Claves Foráneas (Foreign Keys)
    area = models.ForeignKey(
        Area, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Área o Departamento"
    )
    STATUS = models.ForeignKey(
        Status, 
        on_delete=models.PROTECT, 
        verbose_name="Estado del Caso"
    )
    ID_LEVEL = models.ForeignKey(
        Level, 
        on_delete=models.PROTECT, 
        verbose_name="Nivel de Prioridad"
    )
    
    # Campos de Fecha
    CREATION_DATE = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    DATE_FINAL = models.DateField(null=True, blank=True, verbose_name="Fecha de Cierre Estimada")
    
    # Cambiado a DateField con null=True/blank=True
    FECHA_SOLUTION = models.DateField(null=True, blank=True, verbose_name="Fecha de Solución Real") 
    
    SOLUTION = models.CharField(max_length=255, verbose_name="Solución Aplicada")


    class Meta:
        verbose_name = "Reporte de Soporte"
       
        verbose_name_plural = "Reportes de Soporte" 
        # Ordenar por fecha de creación descendente para ver los más nuevos primero
        ordering = ['-CREATION_DATE']

    def __str__(self):
        return f"Reporte #{self.ID_REPORT}: {self.TITLE} ({self.STATUS})"


class Imagenes(models.Model):

    cod_imagen = models.AutoField(primary_key=True)
    
    imagen = models.FileField(
        upload_to='noticias/', 
        max_length=1000, 
        verbose_name="Archivo Adjunto"
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Archivo")
    comentario = models.TextField(max_length=10000, null=True, blank=True, verbose_name="Comentario/Descripción")

    class Meta:
        verbose_name = "Imagen Adjunta"
        verbose_name_plural = "Imágenes Adjuntas"

    def __str__(self):
        return self.nombre