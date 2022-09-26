from functools import total_ordering


class Exam:
    score = 0 
    totalQuestions = 0

    def __init__(self, listOfQuestions):
        self.listOfQuestions = listOfQuestions
        totalQuestions = len(listOfQuestions)

    def score(self, question, answer):
        pass