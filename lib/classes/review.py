from classes.movie import Movie
from classes.viewer import Viewer

class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
