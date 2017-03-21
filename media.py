# A python program to define class Movie

import webbrowser

class Movie():
	"""
	This class defines attributes of movie and also 
	methods to show trailer and a poster 

	movie_title (str) 		- 	Name of the movie
	movie_storyline (str)	-	Plot or summary of the movie 
	poster_image (str)		-	URL to poster image from wikipedia
	trailer_youtube (str)	-	Youtube trailer URL	

	"""

# Defaut constructor definition	
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def show_poster(self):
		webbrowser.open(self.poster_image_url)
