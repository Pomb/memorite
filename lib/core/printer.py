import random
from .settings import printing as settings


class Printer:
    def __init__(self, line_width=settings['line_width']):
        self.line_width = line_width
        self.statements = {
            'correct': [
                'Keep going.',
                'You got it.'],
            'wrong': [
                'Carry on.',
                'Sorry that is incorrect.']
        }

    @property
    def half_line_width(self):
        return int(self.line_width / 2)

    def answer_statement(self, correct=True):
        if correct:
            print('Correct! ' + random.choice(self.statements['correct']))
        else:
            print('Wrong! ' + random.choice(self.statements['wrong']))

    def header(self, out_of):
        print(out_of.center(self.line_width, '-'), '\n')

    def split(self, l, r):
        print(f'{l}{r}')

    def debrief(self, percent, out_of):
        self.centered('Completed')
        self.centered(percent, leading='', char=' ', trailing='\n')

    def lines(self, lines):
        for line in lines:
            print(line)
        print('\n')

    def leave(self):
        self.centered('Good Bye')

    def centered(self, text, leading='\n', char='-', trailing=''):
        print(leading + f' {text} '.center(self.line_width, char) + trailing)

    def line(self, prefix=None):
        return print(prefix + ('▁' * self.line_width), '\n')

    def lineReplaced(self, line, pattern):
        result = line.replace(pattern, '▁')
        print(result)
