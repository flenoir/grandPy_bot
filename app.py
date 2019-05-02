#! /usr/bin/env python
# coding: utf-8

from classes import Question


inputQuestion = input("Please enter your question : ")

new_question = Question(inputQuestion)
print(new_question.tokenize)