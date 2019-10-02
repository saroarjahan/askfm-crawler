class User:

    def __init__(self, _id, name):
        self.id = _id
        self.name = name

    def __repr__(self):
        return f'User({self.name})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


class Article:

    def __init__(self, _id, user, question, answer):
        self.id = _id
        self.user = user
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f'Article({self.question} => {self.answer})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.id == other.id and \
               self.user == other.user and\
               self.question == other.question and\
               self.answer == other.answer
