import pytest

from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer

class TestMovie:
    '''Movie in movie.py'''

    def test_has_title(self):
        '''has the title passed into __init__.'''
        movie = Movie(title="Avatar: The Way of Water")
        assert movie.title == "Avatar: The Way of Water"

    def test_validates_title(self):
        '''has title of string type greater than 0 characters.'''
        with pytest.raises(Exception):
            Movie('')

        with pytest.raises(Exception):
            Movie(1)

    def test_has_class_attribute_all(self):
        '''has a class attribute all which contains all movie instances.'''
        Movie.all = []
        movie1 = Movie('Scarface')
        movie2 = Movie('Aladdin')

        assert movie1 in Movie.all
        assert movie2 in Movie.all
        assert len(Movie.all) == 2
    
    def test_has_reviews(self):
        '''returns a list of its reviews with reviews().'''
        movie = Movie(title="Scarface")
        review = Review(viewer=Viewer("Jeffrey"), movie=movie, rating=1)
        assert review in movie.reviews()

    def test_has_reviewers(self):
        '''returns a list of its reviewers with reviewers().'''
        movie = Movie("Chungking Express")
        viewer = Viewer("William")
        Review(viewer, movie, rating=3)
        assert viewer in movie.reviewers()

    # def test_has_one_review_per_reviewer(self):
    #     '''saves only the most recent review from each viewer with reviews().'''
    #     movie = Movie("Chungking Express")
    #     viewer = Viewer("William")
    #     review = Review(viewer, movie, rating=3)
    #     assert review in movie.reviews()
    #     review2 = Review(viewer, movie, rating=4)
    #     assert review not in movie.reviews()
    #     assert review2 in movie.reviews()

    def test_calculates_average_rating(self):
        '''has a method "average_rating" that returns the average of its ratings.'''
        movie = Movie(title="My Neighbor Totoro")

        Review(viewer=Viewer("username1"), movie=movie, rating=1)
        Review(viewer=Viewer("username2"), movie=movie, rating=3)
        Review(viewer=Viewer("username3"), movie=movie, rating=2)
        Review(viewer=Viewer("username4"), movie=movie, rating=4)
        Review(viewer=Viewer("username5"), movie=movie, rating=5)
        Review(viewer=Viewer("username6"), movie=movie, rating=4)
        Review(viewer=Viewer("username7"), movie=movie, rating=2)
        Review(viewer=Viewer("username8"), movie=movie, rating=3)

        assert movie.average_rating() == 3

    def test_shows_highest_rated(self):
        '''has a classmethod "highest_rated" that returns the highest rated movie.'''
        Movie.all = []
        movie_1 = Movie(title="Avatar: The Way of Water")
        Review(viewer=Viewer("username9"), movie=movie_1, rating=1)
        Review(viewer=Viewer("username10"), movie=movie_1, rating=3)
        Review(viewer=Viewer("username11"), movie=movie_1, rating=2)
        movie_2 = Movie(title="Scarface")
        Review(viewer=Viewer("Katherine"), movie=movie_2, rating=4)
        Review(viewer=Viewer("Catherine"), movie=movie_2, rating=5)
        movie_3 = Movie(title="Rashomon")
        Review(viewer=Viewer("Kathryn"), movie=movie_3, rating=5)
        Review(viewer=Viewer("Katrina"), movie=movie_3, rating=5)
        movie_4 = Movie(title="My Neighbor Totoro")
        Review(viewer=Viewer("Samwise"), movie=movie_4, rating=3)
        assert Movie.highest_rated().title == "Rashomon"
