#! /usr/bin/env python
# coding: utf-8

from mediawiki import MediaWiki
from classes import Question, GoogleMapsSearch

inputQuestion = input("Please enter your question : ")

# instanciation of question
new_question = Question(inputQuestion)
print(new_question.tokenize)


# instanciation of Google maps search from question
new_search = GoogleMapsSearch(new_question.tokenize)
search_result = new_search.makeSearch()

print(search_result)

# instanciation of Mediawiki search
wikipedia = MediaWiki()
wikipedia_result = wikipedia.geosearch(latitude=str(search_result[1]), longitude=str(search_result[2]))

print("He yes, i rememeber that, not very far there's {}".format(wikipedia_result))

