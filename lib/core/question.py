import random


class Question:
    def __init__(self, lines, index, printer, option_count=4, show_lines=4):
        self.lines = lines
        self.option_count = option_count
        self.printer = printer
        self.no_shown_lines = 4
        self.index = index
        self.options = []
        self.answer = None
        self.user_answer = None
        self.is_answered = False
        self.execute()

    @property
    def start_line_index(self):
        return max(self.index - self.no_shown_lines, 0)

    def print_current(self):
        for i in range(self.start_line_index, self.index):
            print(self.lines[i])
        self.printer.line()
        print('\nChoose next line', '\n')

    def execute(self):
        '''Creates options from the given text then asks'''
        self.answer = self.lines[self.index]
        self.options.append(self.answer)
        allow_duplicates = len(self.lines) <= self.option_count

        while len(self.options) < self.option_count:
            randomOption = random.choice(self.lines)
            if randomOption != self.answer:
                if allow_duplicates:
                    self.options.append(randomOption)
                elif randomOption not in self.options:
                    self.options.append(randomOption)

        random.shuffle(self.options)

    def ask(self):
        '''Displays the question and asks for user answer'''
        self.print_current()

        displayOptions = {}
        for i, x in enumerate(self.options):
            displayOptions[str(i + 1)] = x

        result = True

        while not self.is_answered:
            self.display_question()
            choice = input('\nAnswer: ')
            if 'q' == choice:
                result = False
                self.is_answered = True
                break
            if displayOptions.__contains__(choice):
                self.is_answered = True
                self.user_answer = displayOptions[choice]
            else:
                print('\nInvalid option, please try again!\n')

        return result

    def display_question(self):
        '''Prints the options with the numbers'''
        for i, x in enumerate(self.options):
            print(f'{i+1}: {x}')

    def answered_correctly(self):
        '''Compares the users answer with the questions answer'''
        return self.answer == self.user_answer
