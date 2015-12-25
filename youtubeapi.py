import urllib
import json


class YouTubeClient():
    """Connects to YouTube Api
    """

    def __init__(self, apikey):
        """Initiat rest client with Api key
        """

        self.key = apikey
        self.endpoint = "https://www.googleapis.com/youtube/v3/search/?"

    def search_list(self, q):
        """Gets result list for a specific query
    """

        fullq = q + " trailer"
        params = urllib.urlencode(
            {'q': fullq, 'part': 'snippet', 'key': self.key})
        try:
        	connection = urllib.urlopen(self.endpoint + "%s" % params)
        	result = connection.read()
        	return json.loads(result)
        except IOError as err:
        	return False
        
        
