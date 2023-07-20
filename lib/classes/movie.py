class Movie:

    all = []
    
    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 0<len(title):
            self._title = title
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        return [review.viewer for review in self.reviews()]
    
    def average_rating(self):
        ar = [review.rating for review in self.reviews()]
        if len(ar)>0:
            return sum(ar)/len(ar)
        else:
            return 0

    @classmethod
    def highest_rated(cls):
        best_movie = Movie("test")
        for movie in cls.all:
            if movie.average_rating() > best_movie.average_rating():
                best_movie = movie
        return best_movie
    
# This ^ is so ugly but if it works it works 
