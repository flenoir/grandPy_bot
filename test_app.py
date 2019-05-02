from classes import Question

def test_empty_question():
    new_question = Question("where is located openclassrooms ? ")
    assert new_question.tokenize != None

def test_string_question():
    new_question = Question("where is located openclassrooms ? ")
    assert type(new_question.tokenize) is str