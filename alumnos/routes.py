from . import alumnos
from flask import render_template, request, redirect, url_for
import forms

from models import  Alumnos, db

@alumnos.route("/")
def index():
	create_form=forms.UserForm(request.form)
	alumnos = Alumnos.query.all()
	return render_template("alumnos/index.html", form=create_form, alumnos=alumnos)

@alumnos.route('/Alumnos', methods=['GET','POST'])
def crear_alumno():
	create_form=forms.UserForm(request.form)
	if request.method == 'POST':
		alum =Alumnos(nombre=create_form.nombre.data,
					  apellidos=create_form.apellidos.data,
					  email=create_form.email.data,
       				  telefono=create_form.telefono.data,)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        nombre = alum1.nombre
        apellidos = alum1.apellidos
        email = alum1.email
        telefono = alum1.telefono
        cursos = alum1.cursos   
    return render_template(
        'alumnos/detalles.html',
        id=id,
        nombre=nombre,
        apellidos=apellidos,
        email=email,
        telefono=telefono,
        cursos=cursos   # ← ENVIAR CURSOS AL HTML
    )
 
@alumnos.route('/modificar', methods=['GET','POST'])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        alum.telefono = create_form.telefono.data

        db.session.commit()
        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route('/eliminar', methods=['GET','POST'])
def eliminar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=alum1.id
		create_form.nombre.data=alum1.nombre
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
	if request.method=='POST':
		id=create_form.id.data
		alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/eliminar.html", form=create_form)
       
