from . import maestros
from flask import render_template, request, redirect, url_for
import forms

from models import  Maestros, db

@maestros.route("/maestros")
def listado():
    maestros_list = Maestros.query.all()
    return render_template(
        "maestros/listadoMest.html",
        maestros=maestros_list
    )

@maestros.route("/maestros/nuevo", methods=['GET', 'POST'])
def maes():
    create_form = forms.MaestrosForm(request.form)

    if request.method == 'POST':
        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.listado'))

    return render_template("maestros/Maestros.html", form=create_form)

@maestros.route("/maestros/detalles", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id=id
        maes1=db.session.query(Maestros).filter(Maestros.id==id).first()
        nombre=maes1.nombre
        apellidos=maes1.apellidos
        especialidad=maes1.especialidad
        email=maes1.email
    return render_template('maestros/detallesMaes.html', id=id, nombre=nombre,
                       apellidos=apellidos, especialidad=especialidad, email=email)
    
@maestros.route('/maestros/modificar', methods=['GET','POST'])
def modificar():
    create_form = forms.MaestrosForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.id == id).first()
        create_form.id.data = maes1.id
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == 'POST':
        id = create_form.id.data
        maes = db.session.query(Maestros).filter(Maestros.id == id).first()

        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apellidos.data
        maes.especialidad = create_form.especialidad.data
        maes.email = create_form.email.data

        db.session.commit()
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/modificarMaes.html", form=create_form)

@maestros.route('/maestros/eliminar', methods=['GET','POST'])
def eliminar():
	create_form = forms.MaestrosForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		maes1=db.session.query(Maestros).filter(Maestros.id==id).first()
		create_form.id.data=maes1.id
		create_form.nombre.data=maes1.nombre
		create_form.apellidos.data=maes1.apellidos
		create_form.especialidad.data=maes1.especialidad
		create_form.email.data=maes1.email
	if request.method=='POST':
		id=create_form.id.data
		maes=db.session.query(Maestros).filter(Maestros.id==id).first()
		db.session.delete(maes)
		db.session.commit()
		return redirect(url_for('maestros.listado'))
	return render_template("maestros/eliminarMaes.html", form=create_form)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"
