import random
from core.printer import Printer
from core.actions import Action
from core.question.question_factory import QuestionFactory
from utils.helpers import clear


class QuestTrack:
    '''Quest track generates and prompts questions for a length that
    satisfies the number of lines'''
    def __init__(self, lines, num_options, num_shown_lines):
        self.lines = lines
        self.index = 0
        self.correct = 0
        self.printer = Printer()
        self.question_factory = QuestionFactory(
            lines=self.lines,
            num_options=num_options,
            num_shown_lines=num_shown_lines)
        self.question = None

    @property
    def total(self):
        return len(self.lines)

    @property
    def out_of(self):
        return f' {self.index}/{self.total} '

    @property
    def percent(self):
        return f'{self.percent_raw}%'

    @property
    def percent_raw(self):
        return int((self.correct / self.total) * 100)

    def add_score(self, correct):
        if correct:
            self.correct += 1

    @property
    def complete(self):
        return self.index == self.total

    def next(self):
        '''Generates and prompts the next question'''
        self.question = self.question_factory.next(index=self.index)
        complete = False

        while not self.question.is_answered:
            clear()
            self.printer.header(out_of=self.out_of)

            if self.question.ask() == Action.Continue:
                self.add_score(self.question.answered_correctly)
                self.printer.answer_statement(self.question.answered_correctly)
                self.index += 1
                complete = True

        return complete

    def debrief(self):
        self.printer.debrief(
            percent=self.percent,
            out_of=self.out_of)
        self.printer.lines(self.lines)
        print(self.get_progress_message())

    def get_progress_message(self):
        if self.percent_raw < 50:
            return 'Read through the text a couple times and then try again'
        elif self.percent_raw < 75:
            return "Oh It's not great, you need to practice more"
        elif self.percent_raw < 90:
            return "It's close but not close enough, try again"
        elif self.percent_raw < 100:
            return "You so close, You'll get it on your next attempt"
        else:
            return "Well done, you know this text"
