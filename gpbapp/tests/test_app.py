#! /usr/bin/env python
# coding: utf-8

from classes import Question, GoogleMapsSearch, MediaWikiSearch
from mediawiki import MediaWiki
import pytest

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
    assert variable.tokenize == "openclassrooms"
    

def test_empty_result_google():
    new_search = GoogleMapsSearch("le mazet de grand mémé ? ")
    assert new_search.makeSearch() is not None


def test_googlemaps_http_return(monkeypatch):
    results = '260 Chemin des Mendrous, 34170 Castelnau-le-Lez, France'

    def mockreturn(self):        
        return results

    monkeypatch.setattr(GoogleMapsSearch, 'makeSearch', mockreturn)
    new_search = GoogleMapsSearch("le mazet de grand mémé ? ")
    res = new_search.makeSearch()
    assert res == results
    

def test_mediaWiki_openSearch(monkeypatch):
    wiki_res = [('Château de Flaugergues', 'The Château de Flaugergues is a country house near Montpellier, Occitanie, southern France. It is one of many folies erected by wealthy merchants on the outskirts of the city.', 'https://en.wikipedia.org/wiki/Ch%C3%A2teau_de_Flaugergues'), ('Talk:Château de Flaugergues', '', 'https://en.wikipedia.org/wiki/Talk:Ch%C3%A2teau_de_Flaugergues')]

    def mockreturn(self, data):
        return wiki_res

    monkeypatch.setattr(MediaWikiSearch,'make_opensearch', mockreturn)    
    wikipedia = MediaWikiSearch()
    wikipedia_opensearch_result = wikipedia.make_opensearch(str('videomenthe'))

    assert wikipedia_opensearch_result == wiki_res


def test_mediaWiki_geosearch(monkeypatch):
    results = 'Élysée Palace'

    def mockreturn(self, lat, lon):
        return results

    monkeypatch.setattr(MediaWikiSearch,'make_geosearch', mockreturn)    
    new_MediaWiki_search = MediaWikiSearch()
    GeoSearch_result = new_MediaWiki_search.make_geosearch(48.8704156, 2.3167539)

    assert GeoSearch_result == results
