#! /usr/bin/env python
# coding: utf-8

# import nltk
from nltk.corpus import stopwords
import googlemaps
from mediawiki import MediaWiki
from constants import other_words, googleKey
# from gpbapp.views import app (needed to use config.app to import google key from config.py, not working for now)


# nltk.download('stopwords')

en_stopwords = set(stopwords.words('english'))


class Question:
    """ initiate and tokenize question """

    def __init__(self, question):
        self.question = question

    @property
    def tokenize(self):
        mylist = list(self.question.split())

        stopwords_array = [word for word in mylist if word not in en_stopwords]

        other_words_array = [w for w in stopwords_array if w not in other_words]

        print(other_words_array)
        return ' '.join(other_words_array)


class GoogleMapsSearch:
    """ get address and coordinates from tokenized question """

    def __init__(self, search):
        self.search = search


    def makeSearch(self):
        gmaps = googlemaps.Client(key=googleKey)
        try:
            result = gmaps.places(str(self.search))
            result_address = result['results'][0]['formatted_address']
            result_coordinates_lat = result['results'][0]['geometry']['location']['lat']
            result_coordinates_lon = result['results'][0]['geometry']['location']['lng']
            return result_address, result_coordinates_lat, result_coordinates_lon
        except IndexError:
            return "i'm sorry, i don't have a story about this question or maybe you mispelled it"

    # def create_map(self):
    #     gmaps = googlemaps.Client(key=googleKey)
    #     res_map = gmaps.


class MediaWikiSearch:
    """ get informatiosn from MediaWiki """

    def __init__(self):
        pass

    def make_opensearch(self, data):
        wikipedia = MediaWiki()
        wikipedia_opensearch_result = wikipedia.opensearch(str(data))
        return wikipedia_opensearch_result

    def make_geosearch(self, lat, lon):
        wikipedia = MediaWiki()
        wikipedia_result = wikipedia.geosearch(lat, lon)
        opensearch_result = self.make_opensearch(wikipedia_result[0])
        return opensearch_result

    


class Big_search:
    """ make entire search"""

    def __init__(self, question):
        self.question = question
        self.result_object = {}
    
    @property
    def search(self):
        new_question = Question(self.question)
        self.result_object['question'] = new_question.tokenize
        
        # instanciation of Google_search
        new_googlemaps_search = GoogleMapsSearch(new_question.tokenize)
        search_result = new_googlemaps_search.makeSearch()
        self.result_object['google_search_site'] = search_result[0]
        self.result_object['google_search_latitude'] = search_result[1]
        self.result_object['google_search_longitude'] = search_result[2]
        

        # instanciation of MediaWiki search
        new_MediaWiki_search = MediaWikiSearch()
        GeoSearch_result = new_MediaWiki_search.make_geosearch(str(search_result[1]), str(search_result[2]))
        self.result_object['wikipedia_result'] = GeoSearch_result[0][1]
        
        return "Ho yes, {} is located {}.".format(self.result_object['question'].capitalize(), self.result_object['google_search_site']), "I can also say that {}".format(self.result_object['wikipedia_result'])

    
