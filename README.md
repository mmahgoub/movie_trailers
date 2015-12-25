# Movie Trailers
This app will generate an HTML file contains a tile of your favorite movies.


## Configuration
Please add your own YouTube apikey in media.py and own OMDB key in omdbapi.py

## Add Movies
You can add your own movies by creating a new `Movie()` instance in media.py and add it to movies array example: 
```
the_avaitor = media.Movie("The Aviator")
movies = [the_avaitor]
```
You are only required to add the movie title and the app will populate other movie information from [OMDB Api](http://www.omdbapi.com/) and [YouTube API](https://developers.google.com/youtube/)

## Run
To launch this app on a Linux machine please run `$ python fresh_tomatoes.py`