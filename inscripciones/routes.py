from flask import render_template, request, redirect, url_for, flash
from . import inscripciones
from models import db, Alumnos, Curso, Inscripciones
from sqlalchemy.exc import IntegrityError

@inscripciones.route('/inscribirCurso', methods=['GET', 'POST'])
def inscribirCurso():
    alumno_id = request.args.get('id')
    alumno_obj = Alumnos.query.get(alumno_id)

    if request.method == 'POST':
        curso_id = request.form.get('curso_id')

        nueva_inscripcion = Inscripciones(
            alumno_id=alumno_id,
            curso_id=curso_id
        )

        try:
            db.session.add(nueva_inscripcion)
            db.session.commit()
            flash("¡Inscripción realizada con éxito!", "success")
            return redirect(url_for('alumnos.index'))

        except IntegrityError:
            db.session.rollback()
            flash("Este alumno ya está inscrito en ese curso.", "danger")
            return redirect(url_for('alumnos.index'))

    cursos = Curso.query.all()

    return render_template(
        "cursos/inscribirCurso.html",
        cursos=cursos,
        alumno=alumno_obj,
        alumno_id=alumno_id
    )
    
