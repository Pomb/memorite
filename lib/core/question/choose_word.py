import random
from core.printer import Printer
from core.actions import Action
from core.question.question import Question


class ChooseWord(Question):
    def __init__(self, lines, index, num_options, num_shown_lines):
        super().__init__(lines, index)
        self.question_text = 'Choose next word?'
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

    @property
    def allow_duplicates(self):
        return sum([len(x) for x in self.lines]) > len(self.options)

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
        longest_word = self.longest_word(self.options)
        space = len(longest_word) + 1
        q_line = last_line.replace(self.answer, '▁' * space)
        print('\t' + q_line)
        print(f'\nQ: {self.question_text}', '\n')

    def execute(self):
        '''Creates options from the given text then asks'''

        self.answer = random.choice(self.lines[self.index].split())
        self.options.append(self.answer)

        while len(self.options) < self.num_options:
            randomOption = random.choice(random.choice(self.lines).split())
            if randomOption != self.answer:
                if self.allow_duplicates:
                    self.options.append(randomOption)
                elif randomOption not in self.options:
                    self.options.append(randomOption)

        random.shuffle(self.options)

    def ask(self):
        '''Displays the question and asks for user answer'''
        self.print_question()
        self.print_options()

        action = Action.Invalid
        displayOptions = {}
        for i, x in enumerate(self.options):
            displayOptions[str(i + 1)] = x

        choice = input('\nAnswer: ')
        if 'q' == choice:
            action = Action.Quit
            self.is_answered = True
            action = Action.Quit
        elif displayOptions.__contains__(choice):
            self.is_answered = True
            self.user_answer = displayOptions[choice]
            action = Action.Continue
        else:
            print('\nInvalid option, please try again!\n')

        return action

    def print_options(self):
        '''Prints the options with the numbers'''
        for i, x in enumerate(self.options):
            print(f'{i+1}: {x}')
