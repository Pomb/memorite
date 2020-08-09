import random
import string
from core.printer import Printer
from core.actions import Action
from core.question.question import Question
from difflib import SequenceMatcher


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
        s_answer = self.answer.translate(
            str.maketrans('', '', string.punctuation))
        s_user_answer = self.user_answer.translate(
            str.maketrans('', '', string.punctuation))
        accuracy = self.similar(s_answer.lower(), s_user_answer.lower())
        return accuracy > 0.9

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def longest_word(self, words):
        longest = ''
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest

    def average_word_length(self, words):
        return int(len(''.join(words)) / len(words))

    def print_question(self):
        for i in range(self.start_line_index, self.index):
            print('\t' + self.lines[i])
        last_line = self.lines[self.index]
        space = int(self.average_word_length(last_line.split()) * 1.5)
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
