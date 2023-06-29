import random
from questions_storage import get_all_years, get_year


def get_new_question(year=None, previous_question_index=0, shuffle=False):
    index = int(previous_question_index) + 1

    if shuffle:
        question_obj = Question(year)

    else:
        question_obj = Question(year, index)

    return question_obj.get_json()


class Question:

    def __init__(self, year, index=None):
        if not year:
            year = str(random.choice(get_all_years()))

        self.question_object = get_year(year)

        if not index:
            index = random.randint(1, len(self))

        if index == len(self):
            index = 1

        self.index = str(index)
        self.question = self.get_question()
        self.options = self.get_options()
        self.answer = self.get_answer()

    def get_question(self):

        question = self.question_object[self.index]['question']

        if len(question) >= 300:
            question = question[:295] + '...'

        return question

    def get_options(self):

        options = self.question_object[self.index]['options']

        if options:
            random.shuffle(options)

        return options

    def get_answer(self):

        answer = self.question_object[self.index]['answer']

        return answer

    def __len__(self):

        return len(self.question_object)

    def get_json(self):

        return {
            'question_index': self.index,
            'question': self.question,
            'options': self.options,
            'answer': self.answer
        }
