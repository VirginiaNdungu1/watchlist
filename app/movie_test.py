import unittest
# import the movie module
from models import movie
# get the movie class
Movie = movie.Movie
# create a test class


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie Class
    '''

    def setUp(self):
        '''
        Instantiates the Movie Class to make the self.new_movie object
        '''
        self.new_movie = Movie(1234, "Python Must Be Crazy", "A thrilling new Python Series",
                               "https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs", 8.5, 129993)
# define the test case

    def test_instance(self):
        '''
        Uses the isinstance() Function
        Checks if the Object self.new_movie
        is an instance of the Movie Class
        '''
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == "__main__":
    unittest.main()
