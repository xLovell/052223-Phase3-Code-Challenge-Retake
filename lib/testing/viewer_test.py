import pytest

from classes.movie import Movie
from classes.review import Review
from classes.viewer import Viewer

class TestViewer:
    '''Viewer in viewer.py'''

    def test_has_username(self):
        '''has the username passed into __init__.'''
        viewer = Viewer(username="gustave_the_cat")
        assert viewer.username == "gustave_the_cat"

    def test_requires_username_between_6_and_16_characters(self):
        '''requires titles to be strings between 6 and 16 characters, inclusive.'''
        with pytest.raises(Exception):
            Viewer(username="abcde")
        with pytest.raises(Exception):
            Viewer(username=123456)

    # def test_requires_unique_username(self):
    #     '''requires username to be unique.'''
    #     Viewer(username="joey_the_dog")
    #     with pytest.raises(Exception):
    #         Viewer(username="joey_the_dog")

    def test_has_reviews(self):
        '''has method reviews() that adds new reviews and returns a full list of a viewer's reviews'''
        viewer = Viewer(username="fabio_the_hmstr")
        movie = Movie("The Bourne Ultimatum")
        review = Review(viewer, movie, 4)
        assert review in viewer.reviews()

    def test_has_reviewed_movies(self):
        '''has a list of reviewed movies.'''
        viewer = Viewer(username="fanny_the_dog")
        movie = Movie("Bob's Burgers: The Movie")
        Review(viewer, movie, 5)
        assert movie in viewer.reviewed_movies()

    def test_checks_if_has_reviewed_movie(self):
        '''has a method "reviewed_movie" that checks if a movie has been reviewed or not.'''
        viewer = Viewer(username="lucky_the_cat")
        movie_1 = Movie("No Country for Old Men")
        Review(viewer, movie_1, 5)
        assert viewer.has_reviewed_movie(movie_1)
