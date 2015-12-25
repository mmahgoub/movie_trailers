import fresh_tomatoes
import media

"""No need to enter full movie information you just need to enter movie title and all 
other information will be populated automatically even the YouTube trailer URL

This assignment is using no more than functions mentioned during the course except
for json.load()

Enjoy some of my favorite movies!
"""

the_avaitor = media.Movie("The Aviator")
october_sky = media.Movie("October Sky")
american = media.Movie("American Gangster")
social_network = media.Movie("The Social Network")
django = media.Movie("Django Unchained")
gatsby = media.Movie("The Great Gatsby")
gravity = media.Movie("Gravity")
flight = media.Movie("Flight")
enemy = media.Movie("Enemy At the Gates")
im = media.Movie("Inside Man")
wolf = media.Movie("The Wolf of Wall Street")
matrix = media.Movie("The Matrix")

movies = [the_avaitor, october_sky, american, social_network,
          django, gatsby, gravity, flight, enemy, im, wolf, matrix]
fresh_tomatoes.open_movies_page(movies)
