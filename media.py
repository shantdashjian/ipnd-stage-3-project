# Concept: Code reuse by importing a module from Python's Standard Library
import webbrowser

# Concept: User-defined type, encapsualting properties and methods
class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url):
        # Concept: Instance initiation using an 'initiate' method
        # Concpet: Assigning value to instance variable
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url


    def show_trailer(self):
        # Concept: Instance method
        # Concept: Reuse code by clling method from imported module
        webbrowser.open(self.trailer_youtube_url)
