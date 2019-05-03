#! /usr/bin/env python
# coding: utf-8

from classes import Question, GoogleMapsSearch

inputQuestion = input("Please enter your question : ")

# instanciation of question
new_question = Question(inputQuestion)
print(new_question.tokenize)


# instanciation of Google maps search from question
new_search = GoogleMapsSearch(new_question.tokenize)
search_result = new_search.make_search()

print(search_result['results'][0]['formatted_address'])
