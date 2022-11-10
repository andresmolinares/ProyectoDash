# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Alumno(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codestudiantil = models.CharField(db_column='codEstudiantil', max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    identificacion = models.CharField(max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipoDocumento')  # Field name made lowercase.
    digverificacion = models.CharField(db_column='DigVerificacion', max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    nomcompleto = models.CharField(db_column='nomCompleto', max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    prinombre = models.CharField(db_column='priNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segnombre = models.CharField(db_column='segNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    priapellido = models.CharField(db_column='priApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segapellido = models.CharField(db_column='segApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    coddireccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='codDireccion')  # Field name made lowercase.
    celular = models.CharField(max_length=15, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    telefono = models.CharField(max_length=50, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fax = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    correo = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codpensum = models.ForeignKey('Pensum', models.DO_NOTHING, db_column='codPensum')  # Field name made lowercase.
    jornada = models.CharField(max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codescuela = models.ForeignKey('Escuela', models.DO_NOTHING, db_column='codEscuela')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alumno'


class Categoriabienestar(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoriaBienestar'


class Ciudad(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ciudad'


class Configfuente(models.Model):
    campo = models.CharField(max_length=50, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fuente = models.ForeignKey('Fuente', models.DO_NOTHING, db_column='fuente')

    class Meta:
        managed = False
        db_table = 'ConfigFuente'


class Departamento(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamento'


class Deporte(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deporte'


class Detalleprestamo(models.Model):
    codutil = models.CharField(db_column='codUtil', max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    codprestamo = models.ForeignKey('Prestamo', models.DO_NOTHING, db_column='codPrestamo')  # Field name made lowercase.
    fechauso = models.DateTimeField(db_column='fechaUso')  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetallePrestamo'


class Direccion(models.Model):
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigopais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='codigoPais')  # Field name made lowercase.
    codigodep = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='codigoDep')  # Field name made lowercase.
    codigociu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='codigoCiu')  # Field name made lowercase.
    codigozona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='codigoZona')  # Field name made lowercase.
    referncia = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Direccion'


class Entrenador(models.Model):
    estado = models.CharField(max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    identificacion = models.CharField(max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipoDocumento')  # Field name made lowercase.
    digverificacion = models.CharField(db_column='DigVerificacion', max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    nomcompleto = models.CharField(db_column='nomCompleto', max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    prinombre = models.CharField(db_column='priNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segnombre = models.CharField(db_column='segNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    priapellido = models.CharField(db_column='priApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segapellido = models.CharField(db_column='segApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    coddireccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='codDireccion')  # Field name made lowercase.
    celular = models.CharField(max_length=15, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    telefono = models.CharField(max_length=50, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    correo = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fax = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    coddeporte = models.ForeignKey(Deporte, models.DO_NOTHING, db_column='codDeporte')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entrenador'


class Entrenadorhorario(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codentrenador = models.ForeignKey(Entrenador, models.DO_NOTHING, db_column='codEntrenador')  # Field name made lowercase.
    codhorariodep = models.ForeignKey('Horariodeporte', models.DO_NOTHING, db_column='codHorarioDep')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntrenadorHorario'


class Escuela(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Escuela'


class Evento(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codpersonalbie = models.ForeignKey('Personalbienestar', models.DO_NOTHING, db_column='codPersonalBie')  # Field name made lowercase.
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fechainicio = models.DateTimeField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Evento'


class Fuente(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    consecutivo = models.CharField(max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fuente'


class Horariodeporte(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    coddeporte = models.ForeignKey(Deporte, models.DO_NOTHING, db_column='codDeporte')  # Field name made lowercase.
    diadisponible = models.IntegerField(db_column='diaDisponible')  # Field name made lowercase.
    horainicio = models.CharField(db_column='horaInicio', max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    horafin = models.CharField(db_column='horaFin', max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HorarioDeporte'


class Pais(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pais'


class Pensum(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pensum'


class Permiso(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permiso'


class Permisoespecial(models.Model):
    codusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codUsuario')  # Field name made lowercase.
    codpermiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='codPermiso')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PermisoEspecial'


class Permisorol(models.Model):
    codrol = models.CharField(db_column='codRol', max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    codpermiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='codPermiso')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PermisoRol'


class Personalbienestar(models.Model):
    estado = models.CharField(max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    identificacion = models.CharField(max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipoDocumento')  # Field name made lowercase.
    digverificacion = models.CharField(db_column='DigVerificacion', max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    nomcompleto = models.CharField(db_column='nomCompleto', max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    prinombre = models.CharField(db_column='priNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segnombre = models.CharField(db_column='segNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    priapellido = models.CharField(db_column='priApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segapellido = models.CharField(db_column='segApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    coddireccion = models.ForeignKey(Categoriabienestar, models.DO_NOTHING, db_column='codDireccion')  # Field name made lowercase.
    celular = models.CharField(max_length=15, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    telefono = models.CharField(max_length=50, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    correo = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fax = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codcategoria = models.CharField(db_column='codCategoria', max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonalBienestar'


class Prestamo(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fechasolicitud = models.DateTimeField(db_column='fechaSolicitud')  # Field name made lowercase.
    codprestamista = models.ForeignKey('Tercero', models.DO_NOTHING, db_column='codPrestamista', related_name='Prestamo_Prestamist')  # Field name made lowercase.
    codrecibidor = models.ForeignKey('Tercero', models.DO_NOTHING, db_column='codRecibidor', related_name='Prestamo_Recibidor')  # Field name made lowercase.
    codpretador = models.ForeignKey('Tercero', models.DO_NOTHING, db_column='codPretador', related_name='Prestamo_Prestador')  # Field name made lowercase.
    dependecia = models.CharField(max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    totalparti = models.IntegerField(db_column='totalParti')  # Field name made lowercase.
    observacion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prestamo'


class Repositorio(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    ruta = models.CharField(max_length=300, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipomultimedia = models.CharField(db_column='tipoMultimedia', max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    codevento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='codEvento')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Repositorio'


class Rol(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rol'


class Tercero(models.Model):
    estado = models.CharField(max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=10, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codtipoter = models.CharField(db_column='codTipoTer', max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    identificacion = models.CharField(max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipoDocumento')  # Field name made lowercase.
    digverificacion = models.CharField(db_column='DigVerificacion', max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    nomcompleto = models.CharField(db_column='nomCompleto', max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    prinombre = models.CharField(db_column='priNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segnombre = models.CharField(db_column='segNombre', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    priapellido = models.CharField(db_column='priApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    segapellido = models.CharField(db_column='segApellido', max_length=25, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    coddireccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='codDireccion')  # Field name made lowercase.
    celular = models.CharField(max_length=15, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    telefono = models.CharField(max_length=50, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    correo = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    fax = models.CharField(max_length=200, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tercero'


class Tipodocumento(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=5, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoDocumento'


class Tipotercero(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoTercero'


class Usuario(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usuario = models.CharField(unique=True, max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nomusuario = models.CharField(db_column='nomUsuario', unique=True, max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    clave = models.TextField(db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codtercero = models.ForeignKey(Tercero, models.DO_NOTHING, db_column='codTercero')  # Field name made lowercase.
    codrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='codRol')  # Field name made lowercase.
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class Utiles(models.Model):
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=4, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    referencia = models.CharField(max_length=250, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    tipo = models.IntegerField()
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Utiles'


class Zona(models.Model):
    isdian = models.IntegerField(db_column='IsDian')  # Field name made lowercase.
    estado = models.CharField(max_length=1, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    codigo = models.CharField(unique=True, max_length=6, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    nombre = models.CharField(max_length=100, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')
    usersave = models.CharField(db_column='userSave', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechasave = models.DateTimeField(db_column='fechaSave')  # Field name made lowercase.
    usermodify = models.CharField(db_column='userModify', max_length=20, db_collation='Modern_Spanish_100_CI_AS_SC_UTF8')  # Field name made lowercase.
    fechamodify = models.DateTimeField(db_column='fechaModify')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zona'
