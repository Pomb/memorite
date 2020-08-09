import random
from core.printer import Printer
from core.actions import Action
from core.question.question import Question


class TypeWord(Question):
    def __init__(self, lines, index, num_options, num_shown_lines):
        super().__init__(lines, index)
        self.question_text = 'Type the missing word?'
        self.num_options = num_options
        self.num_shown_lines = num_shown_lines
        self.printer = Printer()
        self.answer = None
        self.options = []
        self.user_answer = None
        self.is_answered = False

    @property
    def start_line_index(self):
        return max(self.index - self.num_shown_lines, 0)

    @property
    def answered_correctly(self):
        return self.answer == self.user_answer

    def longest_word(self, words):
        longest = ''
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest

    def print_question(self):
        for i in range(self.start_line_index, self.index):
            print('\t' + self.lines[i])
        last_line = self.lines[self.index]
        longest_word = self.longest_word(last_line.split())
        space = len(longest_word) + 1
        q_line = last_line.replace(self.answer, '▁' * space)
        print('\t' + q_line)
        print(f'\nQ: {self.question_text}', '\n')

    def execute(self):
        '''Creates options from the given text then asks'''
        self.answer = random.choice(self.lines[self.index].split())

    def ask(self):
        '''Displays the question and asks for user answer'''
        self.print_question()

        action = Action.Invalid
        choice = input('\nAnswer: ')

        if 'q' == choice:
            action = Action.Quit
            self.is_answered = True
            action = Action.Quit
        elif len(choice) > 0:
            self.is_answered = True
            self.user_answer = choice
            action = Action.Continue
        else:
            print('\nInvalid option, please try again!\n')

        return action
