import random
from core.printer import Printer
from core.actions import Action
from core.question.question import Question
from utils.helpers import clear


class LineOrder(Question):
    def __init__(self, lines, index, num_options, num_shown_lines):
        self.lines = lines
        self.question_text = '''Re-order the lines.
eg: `1 3` -> Which moves line 1 to position 3'''
        self.num_options = num_options
        self.num_shown_lines = num_shown_lines
        self.printer = Printer()
        self.index = index
        self.answer = []
        self.options = []
        self.is_answered = False

    @property
    def start_line_index(self):
        return max(self.index - self.num_shown_lines, 0)

    @property
    def answered_correctly(self):
        return self.options == self.answer

    def print_question(self):
        for i in range(self.start_line_index, self.index):
            print('\t' + self.lines[i])
        print(f'\nQ: {self.question_text}', '\n')

    def execute(self):
        '''Creates options from the given text then asks'''
        counter = 0
        # bring the counter back if it's going to run out of bounds
        if self.index + self.num_options > len(self.lines):
            diff = len(self.lines) - (self.index + self.num_options)
            counter = diff

        while len(self.options) < self.num_options:
            index = self.index + counter
            option = self.lines[index]
            self.options.append(option)
            self.answer.append(option)
            counter += 1
            if counter > len(self.lines):
                break

        while self.options == self.answer:
            random.shuffle(self.options)

    def ask(self):
        '''Displays the question and asks for user answer'''
        action = Action.Invalid
        nums = [str(i) for i in range(1, self.num_options + 1)]

        self.print_question()
        self.print_options()

        choice = input('\nAnswer: ')
        if 'q' == choice:
            self.is_answered = True
            action = Action.Quit
        elif 'a' in choice:
            self.is_answered = True
            action = Action.Continue
        else:
            try:
                splits = choice.split()
                c_index = splits[0]
                c_target = splits[1]
                if c_index in nums and c_target in nums:
                    index = int(c_index) - 1
                    target = int(c_target) - 1
                    line = self.options[index]
                    self.options.pop(index)
                    self.options.insert(target, line)
                    action = Action.Continue
                else:
                    input('\nInvalid option, please type numbers!')
            except:
                input('\nInvalid option, please try again!')

        return action

    def print_options(self):
        for i, x in enumerate(self.options):
            print(f'{i + 1}: {self.options[i]}')
        print('\na: Accept')
