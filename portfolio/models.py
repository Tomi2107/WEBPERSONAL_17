from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(verbose_name = 'imagen', upload_to ="projects")
    link = models.URLField(verbose_name = 'Dirección web', null = True, blank= True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'fecha de modificación')
   
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
    
     
    def __str__(self):
        return self.title