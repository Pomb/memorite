import random


class Question:
    def __init__(self, lines, index, optionCount=4):
        self.lines = lines
        self.optionCount = optionCount
        self.index = index
        self.options = []
        self.answer = None
        self.userAnswer = None
        self.isAnswered = False

    def execute(self):
        '''Creates options from the given text then asks'''
        self.answer = self.lines[self.index]
        self.options.append(self.answer)
        allow_duplicates = len(self.lines) <= self.optionCount

        while len(self.options) < self.optionCount:
            randomOption = random.choice(self.lines)
            if randomOption != self.answer:
                if allow_duplicates:
                    self.options.append(randomOption)
                elif randomOption not in self.options:
                    self.options.append(randomOption)

        random.shuffle(self.options)

    def ask(self):
        '''Takes a question object and asks'''
        displayOptions = {}
        for i, x in enumerate(self.options):
            displayOptions[str(i + 1)] = x
        
        result = True
        
        while not self.isAnswered:
            self.displayQuestion()
            choice = input('\nchoose an answer: ')
            if 'q' == choice:
                result = False
                self.isAnswered = True
                break
            if displayOptions.__contains__(choice):
                self.isAnswered = True
                self.userAnswer = displayOptions[choice]
            else:
                print('\nInvalid option, please try again!\n')

        return result

    def displayQuestion(self):
        for i, x in enumerate(self.options):
            print(f'{i+1}: {x}')

    def answeredCorrectly(self):
        '''compares the answer with the question'''
        return self.answer == self.userAnswer
