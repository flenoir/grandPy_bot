import nltk
from nltk.corpus import stopwords

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

