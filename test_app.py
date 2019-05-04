from classes import Question, GoogleMapsSearch
import pytest

@pytest.fixture
def variable():
    input_question = "where is located openclassrooms ? "
    new_question = Question(input_question)
    return new_question


def test_empty_question(variable):
    assert variable.tokenize != None

def test_string_question(variable):    
    assert type(variable.tokenize) is str

def test_tokenization_question(variable):
    assert variable.tokenize  == "located openclassrooms ?"
    

def test_empty_result_google():
    new_search = GoogleMapsSearch("search string")
    assert new_search.make_search() != None