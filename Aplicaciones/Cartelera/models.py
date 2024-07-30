from django.db import models

# Creando modelo Genero: terror, comedia.

# Base de datos principal es CARTELERA

# Creación de las tablas 
class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150,default='')
    foto=models.FileField(upload_to='generos', null=True, blank=True)
    def __str__(self):
        #Estructura para una fila y me salga la descripción de cada dato que voy a ingresar
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)

class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    apellido=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores', null=True, blank=True)
    def __str__(self):
        #Estructura para una fila y me salga la descripción de cada dato que voy a ingresar
        fila="{0}: {3} - {2}"
        return fila.format(self.id,self.dni,self.apellido,self.nombre,self.estado)

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    continente=models.CharField(max_length=50)
    capital=models.CharField(max_length=50)
    def __str__(self):
        #Estructura para una fila y me salga la descripción de cada dato que voy a ingresar
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.continente,self.capital)
    
class Peliculas(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.CharField(max_length=80, null=False)
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    director=models.ForeignKey(Director,on_delete=models.CASCADE)
    portada=models.FileField(upload_to='portadas', null=True, blank=True)
    #método str self --> diferecciando a la propia clase, para llamar al atributo
    
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.titulo)
    
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25, null=False)
    direccion=models.CharField(max_length=150, null=False)
    telefono=models.CharField(max_length=80, null=False)
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.nombre,self.direccion)
    