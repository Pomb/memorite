import random
from .settings import printing as settings


class PrettyPrint:
    def __init__(self, line_width=settings['line_width']):
        self.line_width = line_width
        self.statements = {
            'correct': [
                'Good going.',
                'Yes you got it'],
            'wrong': [
                'You answered incorrectly.',
                "Sorry that was incorrect."]
        }

    @property
    def half_line_width(self):
        return int(self.line_width / 2)

    def answer_statement(self, correct=True):
        if correct:
            print('Correct! ' + random.choice(self.statements['correct']))
        else:
            print('Wrong! ' + random.choice(self.statements['wrong']))

    def header(self, score_keeper):
        percent = f'{score_keeper.percent}%'
        out_of = f'{score_keeper.index + 1} of {score_keeper.total + 1}'
        hr = percent.rjust(self.half_line_width, ' ')
        hl = out_of.ljust(self.half_line_width, ' ')
        self.split(hl, hr)
        print(''.center(self.line_width, '-'), '\n')

    def split(self, l, r):
        print(f'{l}{r}')

    def debrief(self, score_keeper):
        percent = f'{score_keeper.percent}%'
        out_of = score_keeper.out_of
        hr = percent.rjust(self.half_line_width, ' ')
        hl = out_of.ljust(self.half_line_width, ' ')
        self.split(hl, hr)
        self.centered('Completed')

    def lines(self, lines):
        for line in lines:
            print(line)
        print('\n')

    def leave(self):
        self.centered('Good Bye')

    def centered(self, text):
        print('\n' + f' {text} '.center(self.line_width, '-') + '\n')

    def line(self, prefix=None):
        print('_' * self.line_width, '\n')