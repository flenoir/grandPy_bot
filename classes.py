#! /usr/bin/env python
# coding: utf-8

import nltk
from nltk.corpus import stopwords
import googlemaps
from mediawiki import MediaWiki

# nltk.download('stopwords')

en_stopwords = set(stopwords.words('english'))


class Question:
    """
    initiate and tokenize question
    """

    def __init__(self, question):
        self.question = question

    @property
    def tokenize(self):
        mylist = list(self.question.split())
        array = []

        for word in mylist:
            if word not in en_stopwords:
                array.append(word)
        
        print (array)
        return ' '.join(array)


class GoogleMapsSearch:
    """
    get address and coordintates from tokenized question
    """

    KEY = 'AIzaSyCnu18GjJrqGyvQ3DMECincwFAslFeGTu4'

    def __init__(self, search):
        self.search = search
      
    
    def makeSearch(self):
        gmaps = googlemaps.Client(key=GoogleMapsSearch.KEY)
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