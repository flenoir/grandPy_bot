#! /usr/bin/env python
# coding: utf-8

from classes import Question, GoogleMapsSearch, MediaWikiSearch

inputQuestion = input("Please enter your question : ")

# instanciation of question
new_question = Question(inputQuestion)
print(new_question.tokenize)


# instanciation of Google maps search from question
new_search = GoogleMapsSearch(new_question.tokenize)
search_result = new_search.makeSearch()

print(search_result)

# instanciation of MediaWiki search
new_MediaWiki_search = MediaWikiSearch()
GeoSearch_result = new_MediaWiki_search.make_geosearch(str(search_result[1]), str(search_result[2]))

# wikipedia_result = mediaWikiSearch(search_result[1], search_result[2])
print(GeoSearch_result[0])

print("He yes, i remember that, not very far there's a place called {}".format(GeoSearch_result[0]))

# opensearch_result = wikipedia.opensearch(str(wikipedia_result[0]))

# print("In details, {}".format(opensearch_result[0][1]))

