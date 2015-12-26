import webbrowser
import omdbapi
import youtubeapi


class Movie():

    def __init__(self, movie_title):
        # setting instance vars
        client = omdbapi.RestClient()
        result = client.get_movie(movie_title)
        if(result):
            self.title = result["Title"]
            self.storyline = result["Plot"]
            self.poster_image_url = result["Poster"]
            self.year = result["Year"]
            self.genre = result["Genre"]

            ytclient = youtubeapi.YouTubeClient(
            "AIzaSyCtsDlez_k470KAH8LKK0ZE6MTTXynXO9E")
            search_result = ytclient.search_list(self.title)
            self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + \
            search_result["items"][0]["id"]["videoId"]
        else:
        	self.title = 'Not Found!'
        	self.storyline = ''
        	self.poster_image_url = ''
        	self.year = ''
        	self.genre = ''
        	# Something to cheer you up!
        	self.trailer_youtube_url = 'https://www.youtube.com/watch?v=jofNR_WkoCE'

    # opens browser to display youtube trailer page
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
