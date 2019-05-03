import nltk
from nltk.corpus import stopwords
import googlemaps

en_stopwords = set(stopwords.words('english'))

class Question:

    def __init__(self, question):
        self.question = question

    @property
    def tokenize(self):
        mylist = list(self.question.split())
        array = []

        for word in mylist:
            if word not in en_stopwords:
                array.append(word)
        
        return ' '.join(array)


class GoogleMapsSearch:

    KEY = 'AIzaSyCnu18GjJrqGyvQ3DMECincwFAslFeGTu4'

    def __init__(self, search):
        self.search = search
      
    
    def make_search(self):
        gmaps = googlemaps.Client(key=GoogleMapsSearch.KEY)
        result = gmaps.places(str(self.search))
        return result

