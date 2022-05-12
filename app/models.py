class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.vote_count = vote_count
        self.vote_average = vote_average
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster



class Review:
    '''
    Movie class to define Review Objects
    '''

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id

        self.title = title
        self.review = review
        self.imageurl = imageurl


    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response