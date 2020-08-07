import random
from core.printer import Printer
from core.actions import Action
from core.question.question_factory import QuestionFactory


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
        return f'{self.index}/{self.total}'

    @property
    def percent(self):
        p = int((self.correct / self.total) * 100)
        return f'{p}%'

    def add_score(self, correct):
        if correct:
            self.correct += 1

    @property
    def complete(self):
        return self.index == self.total

    def next(self):
        '''Generates and prompts the next question'''
        self.printer.header(
            percent=self.percent,
            out_of=self.out_of)

        self.question = self.question_factory.next(index=self.index)

        if self.question.ask() == Action.Continue:
            self.add_score(self.question.answered_correctly)
            self.printer.answer_statement(self.question.answered_correctly)
            self.index += 1
            return True
        else:
            return False

    def debrief(self):
        self.printer.debrief(
            percent=self.percent,
            out_of=self.out_of)
        self.printer.lines(self.lines)
