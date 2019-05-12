#! /usr/bin/env python
# coding: utf-8

import nltk
from nltk.corpus import stopwords
import googlemaps
from mediawiki import MediaWiki
from constants import other_words, googleKey
# from gpbapp.views import app (needed to use config.app to import google key from config.py, not working for now)


# nltk.download('stopwords')

en_stopwords = set(stopwords.words('english'))


class GoogleMapsSearch:
    """
    get address and coordintates from tokenized question
    """

    def __init__(self, search):
        self.search = search
      
    
    def makeSearch(self):
        gmaps = googlemaps.Client(key=googleKey)
        result = gmaps.places(str(self.search))
        result_address = result['results'][0]['formatted_address']
        result_coordinates_lat = result['results'][0]['geometry']['location']['lat']
        result_coordinates_lon = result['results'][0]['geometry']['location']['lng']
        return result_address, result_coordinates_lat, result_coordinates_lon


class MediaWikiSearch:

    def __init__(self):
        pass

    def make_geosearch(self, lat, lon):
        wikipedia = MediaWiki()
        wikipedia_result = wikipedia.geosearch(lat, lon)
        return wikipedia_result


class Question:
    """
    initiate and tokenize question
    """

    def __init__(self, question):
        self.question = question

    @classmethod   
    def google_request(self, v):
        # instanciation of Google maps search from question
        new_search = GoogleMapsSearch(v)
        search_result = new_search.makeSearch()
        return search_result
        

    @property
    def tokenize(self):
        mylist = list(self.question.split())

        stopword_array = [word for word in mylist if word not in en_stopwords]
        other_words_array = [w for w in stopword_array if w not in other_words]
        
        joined_array = ' '.join(other_words_array)
        google_search = self.google_request(joined_array)        
        return google_search

  

