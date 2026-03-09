from flask import render_template, request, redirect, url_for
from . import cursos
from models import Curso, Maestros, db
import forms

@cursos.route("/cursos")
def listado():
    cursos_list = Curso.query.all()
    return render_template(
        "cursos/listadocursos.html",
        cursos=cursos_list
    )
   
@cursos.route("/cursos/nuevo", methods=['GET', 'POST'])
def curso():
    create_form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, m.nombre) for m in maestros]
    if request.method == 'POST':
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.listado'))
    return render_template("cursos/Cursos.html", form=create_form)
    
@cursos.route('/cursos/modificar', methods=['GET','POST'])
def modificar():
    create_form = forms.CursoForm(request.form)

    if request.method == 'GET':
        curso_id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == curso_id).first()
        create_form.nombre.data = cur.nombre
        create_form.descripcion.data = cur.descripcion
        maestros = Maestros.query.all()
        create_form.maestro_id.choices = [(m.matricula, m.nombre) for m in maestros]

    if request.method == 'POST':
        id = request.form.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()

        cur.nombre = create_form.nombre.data
        cur.descripcion = create_form.descripcion.data
        cur.maestro_id = create_form.maestro_id.data

        db.session.commit()
        return redirect(url_for('cursos.listado'))

    return render_template("cursos/modificarCur.html", form=create_form)

@cursos.route("/cursos/detalles", methods=['GET'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        nombre = cur.nombre
        descripcion = cur.descripcion
        maestro = f"{cur.maestro.nombre} {cur.maestro.apellidos}"
    return render_template('cursos/detallesCur.html',                      
                            id=id,
                            nombre=nombre,
                            descripcion=descripcion,
                            maestro=maestro)
    
@cursos.route('/cursos/eliminar', methods=['GET','POST'])
def eliminar():
    create_form = forms.CursoForm(request.form)
    maestros = db.session.query(Maestros).all()
    create_form.maestro_id.choices = [(m.matricula, m.nombre) for m in maestros]
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.nombre.data = cur.nombre
        create_form.descripcion.data = cur.descripcion
        create_form.maestro_id.data = cur.maestro_id
    if request.method == 'POST':
        id = request.form.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        db.session.delete(cur)
        db.session.commit()
        return redirect(url_for('cursos.listado'))
    return render_template("cursos/eliminarCur.html", form=create_form)

@cursos.route('/cursos/alumnosins')
def alumnosins():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id).first()
    alumnos = curso.alumnos
    return render_template(
        "cursos/alumnosinscritos.html",
        curso=curso,
        alumnos=alumnos
    )

