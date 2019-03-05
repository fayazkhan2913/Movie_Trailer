import webbrowser

class Tollytrailers():
    def __init__(self,movie_title,movie_storyline,movie_poster_url,movie_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_url=movie_poster_url
        self.trailers_youtube=movie_youtube
    def show_movie_trailers(self):
        webbrowser.open(self.trailers_youtube)
        
