import random
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
import sqlalchemy
from main.forms import CreateListForm
from main.omdb_util import get_movie_detail, list_movies_by_search
from models import db, MovieList, Movie
from main import constants, main


@main.route("/")
@main.route("/home")
@login_required
def home():
    lists = MovieList.query.filter_by(user_id=current_user.id).all()
    form = CreateListForm()

    slides_sample = random.sample(sorted(constants.MOVIE_WALLPAPERS), 4)
    slides = {k: constants.MOVIE_WALLPAPERS[k] for k in slides_sample}
    return render_template("home.html", lists=lists, form=form, movies_slides=slides)


@main.route("/search/<int:list_id>/<int:page>", methods=["POST"])
@login_required
def search(list_id, page=1):
    movie_list = MovieList.query.get_or_404(list_id)
    movies = list_movies_by_search(query=request.form["query"], page=page)
    return render_template(
        "movie_list.html",
        list=movie_list,
        movies=movies,
        curr_page=page,
        prev_query=request.form["query"],
    )


@main.route("/add_movie", methods=["POST"])
@login_required
def add_movie():
    page = int(request.form["page"])
    query = request.form["query"]

    movie_title = request.form["title"]
    movie_year = request.form["year"]
    imdb_id = request.form["imdb_id"]
    list_id = request.form["list_id"]

    movie = Movie(title=movie_title, year=movie_year, imdb_id=imdb_id, list_id=list_id)
    try:
        db.session.add(movie)
        db.session.commit()
        flash("Movie added to the list!", "success")

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        flash("Movie already exists in the list!", "danger")

    movie_list = MovieList.query.get_or_404(list_id)
    movies = list_movies_by_search(query=query, page=page)
    return render_template(
        "movie_list.html",
        list=movie_list,
        movies=movies,
        curr_page=page,
        prev_query=query,
    )


@main.route("/create_list", methods=["POST"])
@login_required
def create_list():
    list_title = request.form["title"]
    movie_list = MovieList(title=list_title, author=current_user)
    db.session.add(movie_list)
    db.session.commit()
    flash("Movie list created!", "success")

    return redirect(url_for("main.home"))


@main.route("/list/<int:list_id>")
@login_required
def view_list(list_id):
    movie_list = MovieList.query.get_or_404(list_id)
    return render_template("movie_list.html", list=movie_list)


@main.route("/movie/<string:imdb_id>")
@login_required
def movie_detail(imdb_id):
    detail = get_movie_detail(imdb_id)
    return render_template("movie_detail.html", detail=detail)


@main.route("/delete_movie/<int:list_id>/<string:imdb_id>", methods=["GET"])
@login_required
def delete_movie(list_id, imdb_id):
    movie = Movie.query.filter_by(list_id=list_id, imdb_id=imdb_id).first()
    if movie:
        db.session.delete(movie)
        db.session.commit()
        flash("Movie deleted from the list!", "success")
    else:
        flash("Movie not found in the list!", "danger")
    return redirect(url_for("main.view_list", list_id=list_id))
