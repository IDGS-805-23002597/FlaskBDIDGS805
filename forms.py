from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, TextAreaField, SelectField
from wtforms import EmailField
from wtforms import validators
from wtforms.validators import Optional

class UserForm(FlaskForm):
    id=IntegerField("id",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("nombre",
    [validators.DataRequired(message="El campo es requerido"),
     validators.length(min=4, max=10, message="El campo es requerido")])
    
    apellidos=StringField("apellidos",
    [validators.DataRequired(message="El campo es requerido")])

    email=EmailField("coreo",
    [validators.Email(message="Ingresa un correo valido")])
    
    telefono=StringField("telefono",
    [validators.DataRequired(message="Ingresa un telefono valido")])
    
class MaestrosForm(FlaskForm):
    matricula=IntegerField("matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("nombre",
    [validators.DataRequired(message="El campo es requerido"),
     validators.length(min=4, max=50, message="El campo es requerido")])
    
    apellidos=StringField("apellidos",
    [validators.DataRequired(message="El campo es requerido")])

    especialidad=StringField("especialidad",
    [validators.DataRequired(message="Ingresa un correo valido")])
    
    email=EmailField("correo",
    [validators.Email(message="Ingresa un correo valido")])

class CursoForm(FlaskForm):
    nombre = StringField("Nombre del Curso",
    [validators.DataRequired(message="El campo es requerido"),
     validators.length(min=4, max=50, message="El campo es requerido")])
    
    descripcion = TextAreaField("Descripción")
    
    maestro_id = SelectField("Maestro Asignado", coerce=int, validators=[validators.DataRequired()])
    
class InscripcionForm(FlaskForm):
    id = IntegerField("ID Inscripción", validators=[validators.Optional()])
    
    alumno_id = StringField("Alumno", [
        validators.DataRequired(message="Debe seleccionar un alumno")
    ])
    
    curso_id = StringField("Curso", [
        validators.DataRequired(message="Debe seleccionar un curso")
    ])
    
    