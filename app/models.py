class Movie:
    '''
    Movie Class to define Movie Objects
    '''

    def __init__(self, id, title, overview, image, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.image = 'http://image.tmdb.org/t/p/w500' + image
        self.vote_average = vote_average
        self.vote_count = vote_count


class Reviews:
    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        '''
        method that appends the review object
        to a class variable class all_reviews
        which is an empty list
        '''

        Reviews.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Reviews.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
        '''
        method takes an id
        it loops through the all_reviews list
        checks for reviews that have the same movie ID as the id
        if True: append those reviews to a new response list
        return that response list
        '''
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response
