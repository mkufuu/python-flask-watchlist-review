from flask import render_template
from .request import get_movies
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    latest_movies = get_movies('upcoming')

    popular_movies = get_movies('popular')

    return render_template('index.html', latest_movies = latest_movies, popular_movies = popular_movies)

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')