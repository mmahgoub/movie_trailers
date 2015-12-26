import urllib
import json


class RestClient():
    """A Restful client for OMDB Api
    """

    def __init__(self):
        self.apikey = "14c840d6"
        self.endpoint = "http://www.omdbapi.com/?"

    def get_movie(self, title):
        """Gets full movie information
    """

        params = urllib.urlencode(
            {'t': title, 'plot': 'short', 'r': 'json', 'apikey': self.apikey})
        try:
        	connection = urllib.urlopen(self.endpoint + "%s" % params)
        	result = connection.read()
        	return json.loads(result)
        except IOError as err:
        	return False