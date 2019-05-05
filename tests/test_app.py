#! /usr/bin/env python
# coding: utf-8

from classes import Question, GoogleMapsSearch
import pytest
import urllib.request

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


def test_http_return(monkeypatch):
    results = '260 Chemin des Mendrous, 34170 Castelnau-le-Lez, France'

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    new_search = GoogleMapsSearch("le mazet de grand mémé ? ")
    res = new_search.makeSearch()
    assert res[0] == results
