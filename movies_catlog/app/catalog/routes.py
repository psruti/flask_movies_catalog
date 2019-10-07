from app.catalog import main
from app import db
from app.catalog.models import Movie, Production
from flask import render_template, request, redirect, url_for, flash
from app.catalog.forms import EditMovieForm, CreateMovieForm
from flask_login import login_required


@main.route('/')
def display_movies():
    movies = Movie.query.all()
    return render_template('home.html', movies=movies)
@main.route('/display/production/<production_id>')
def display_production(production_id):
    production = Production.query.filter_by(id=production_id).first()
    production_movies = Movie.query.filter_by(prod_id = production.id).all()

    return render_template('production.html', production=production, production_movies=production_movies)

@main.route('/movie/delete/<movie_id>', methods=['GET', 'POST'])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        flash('Movie deleted successfully')
        return redirect(url_for('main.display_movies'))
    return render_template('delete_movie.html', movie=movie, movie_id=movie.id)

@main.route('/edit/movie/<movie_id>', methods=['GET', 'POST'])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    form = EditMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.name = form.name.data
        movie.cast = form.cast.data
        movie.directors = form.directors.data
        db.session.add(movie)
        db.session.commit()
        flash('Movie Edited Successfully')
        return redirect(url_for('main.display_movies'))
    return render_template('edit_movie.html', form=form)


@main.route('/create/movie/<prod_id>', methods=['GET', 'POST'])
@login_required
def create_movie(prod_id):
    form = CreateMovieForm()
    form.prod_id.data = prod_id  # pre-populates pub_id
    if form.validate_on_submit():
        movie = Movie(name=form.name.data, directors=form.directors.data, cast=form.cast.data, avg_rating=form.avg_rating.data,
                     image=form.img_url.data, prod_id=form.prod_id.data)
        db.session.add(movie)
        db.session.commit()
        flash('Movie added successfully')
        return redirect(url_for('main.display_production', production_id=prod_id))
    return render_template('create_movie.html', form=form, prod_id=prod_id)