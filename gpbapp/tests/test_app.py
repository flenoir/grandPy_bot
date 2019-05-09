#! /usr/bin/env python
# coding: utf-8

from classes import Question, GoogleMapsSearch, MediaWikiSearch
import pytest
# import urllib.request
# from mediawiki import MediaWiki

@pytest.fixture
def variable():
    input_question = "where is located openclassrooms ? "
    new_question = Question(input_question)
    return new_question


def test_empty_question(variable):
    assert variable.tokenize is not None


def test_string_question(variable):    
    assert type(variable.tokenize) is str


def test_tokenization_question(variable):
    assert variable.tokenize == "located openclassrooms ?"
    

def test_empty_result_google():
    new_search = GoogleMapsSearch("le mazet de grand mémé ? ")
    assert new_search.makeSearch() is not None


# def test_googlemaps_http_return(monkeypatch):
#     results = '260 Chemin des Mendrous, 34170 Castelnau-le-Lez, France'

#     def mockreturn(request):
#         print('bonjour1')
#         return results

#     monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
#     new_search = GoogleMapsSearch("le mazet de grand mémé ? ")
#     res = new_search.makeSearch()
#     assert res[0] == results
    

# def test_mediawiki_geosearch_http_return(monkeypatch):
#     results = 'Élysée Palace'

#     def mockreturn(request):
#         print('bonjour2')
#         return results

#     monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)    
#     wikipedia = MediaWiki()
#     wikipedia_results = wikipedia.geosearch(latitude=48.8704156, longitude=2.3167539)
#     assert wikipedia_results[0] == results
    
def test_mediaWikiSearch(monkeypatch):
    results = 'Élysée Palace'

    def mockreturn(self, lat, lon):
        return results

    monkeypatch.setattr('mediawiki.MediaWiki.geosearch', mockreturn)    
    new_MediaWiki_search = MediaWikiSearch()
    GeoSearch_result = new_MediaWiki_search.make_geosearch(48.8704156, 2.3167539)

    assert GeoSearch_result == results
