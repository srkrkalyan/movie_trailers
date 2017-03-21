# A Python program to create instances of class movie and save various
# attributes
# This program uses Wikipedia API to retrieve poster image and movie plot

import wikipedia
import fresh_tomatoes
import re
import media

# This function uses wikipedia API to retrieve movier poster image
# Function to retrieve poster image URL from wikipedia by passing
# movie name as argument
# This function will also use Python regular expressions to filter
# out poster URL from the list of image
# urls returned by wikipedia API


def get_poster_url(movie_name):
    poster_url = None
    movie_name = movie_name + " (film) "
    # Calling wikipedia API
    movie_page = wikipedia.page(movie_name)
    list_of_images = movie_page.images
    for image_url in list_of_images:
        # Using regular expressions to filter out correct URL
        match = re.search("[pP]oster", image_url)
        if match:
            poster_url = image_url
            # Terminate if correct URL is found
            break
    return poster_url

# This function uses wikipedia API to retrieve movie summary
# Function to retrieve movie summary from wikipedia by passing movie
# name as argument


def get_movie_plot(movie_name):
    movie_name = movie_name + " (film) "
    movie_page = wikipedia.page(movie_name)
    movie_summary = movie_page.summary
    return movie_summary

# Creating various instances of class Movie

jurassic_park = media.Movie("Jurassic Park", get_movie_plot("Jurassic Park"),
                            get_poster_url("Jurassic Park"),
                            "https://www.youtube.com/watch?v=lc0UehYemQA")


school_of_rock = media.Movie("School Of Rock",
                             get_movie_plot("School Of Rock"),
                             get_poster_url("School Of Rock"),
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

night_at_the_museum = media.Movie(
    "Night At The Museum",
    get_movie_plot("Night at the museum"),
    get_poster_url("Night at the museum"),
    "https://www.youtube.com/watch?v=yc-N-7FD9oA")

the_martian = media.Movie("The Martian",
                          get_movie_plot("The Martian"),
                          get_poster_url("The Martian"),
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

life_of_pi = media.Movie("Life of Pi",
                         get_movie_plot("Life of pi"),
                         get_poster_url("Life of Pi"),
                         "https://www.youtube.com/watch?v=mZEZ35Fhvuc")

despicable_me = media.Movie("Despicable Me",
                            get_movie_plot("Despicable Me"),
                            get_poster_url("Despicable Me"),
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

# Creating the list of movie objects created above

movies_list = [jurassic_park, school_of_rock, night_at_the_museum,
               the_martian, life_of_pi, despicable_me]

# Calling open_movies_page function by passing movies list to create HTML file

fresh_tomatoes.open_movies_page(movies_list)
