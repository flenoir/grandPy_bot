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


class Question:
    """
    initiate and tokenize question
    """

    def __init__(self, question):
        self.question = question

    @property
    def tokenize(self):
        mylist = list(self.question.split())
        # array = []

        # for word in mylist:
        #     if word not in en_stopwords:
        #         array.append(word)

        array = [word for word in mylist if word not in en_stopwords]

        array2 = [w for w in array if w not in other_words]
        
        print(array2)
        return ' '.join(array2)


class GoogleMapsSearch:
    """
    get address and coordintates from tokenized question
    """

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

        


class MediaWikiSearch:

    def __init__(self):
        pass

    def make_geosearch(self, lat, lon):
        wikipedia = MediaWiki()
        wikipedia_result = wikipedia.geosearch(lat, lon)
        return wikipedia_result


class Big_search:

    def __init__(self, question):
        self.question = question
    
    @property
    def search(self):
        new_question = Question(self.question)
        new_googlemaps_search = GoogleMapsSearch(new_question.tokenize)
        return new_googlemaps_search.makeSearch()
    
