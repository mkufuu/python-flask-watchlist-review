from .models import Movie
import urllib.request,json

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def process_results(collection):
    movie_results = []

    for item in collection:
        id = item.get('id')
        overview = item.get('overview')
        poster = item.get('poster_path')
        title = item.get('original_title')
        vote_count = item.get('vote_count')
        vote_average = item.get('vote_average')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

            movie_results.append(movie_object)

    return movie_results

def get_movies(category):
    get_movies_url = f"{base_url}/{category}?api_key={api_key}"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results