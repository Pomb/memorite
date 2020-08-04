import sys
import os
import random
from core.question import Question


line_width = 20
half_line_width = int(line_width / 2)


class App:
    def __init__(self, textFile, no_shown_lines=4):
        self.enabled = True
        self.no_shown_lines = no_shown_lines
        self.textFile = textFile
        self.lines = None
        self.index = 0
        self.correct = 0
        self.statements = {
            'correct': [
                'Awe yeah you answered correctly!', 'You got it!',
                'Nailed it!', "Yes, one for the bag!"],
            'wrong': [
                'Nope, you answered incorrectly!',
                'No that was wrong.', "Sorry, that was incorrect."]
        }

    @property
    def start_line_index(self):
        return max(self.index - self.no_shown_lines, 0)

    def print_header(self):
        percent = f'{int(self.correct / len(self.lines) * 100)}%'
        out_of = f'{self.correct}/{len(self.lines)}'
        hr = percent.rjust(half_line_width, ' ')
        hl = out_of.ljust(half_line_width, ' ')
        print(f'{hl}{hr}')
        print(''.center(line_width, '-'), '\n')

    def run(self):
        print(f'run app on {self.textFile}')
        rawText = ''
        with open(self.textFile, 'r') as f:
            rawText = f.read()
        self.lines = rawText.split('\n')

        while(self.enabled):
            clearScreen()
            self.print_header()

            for i in range(self.start_line_index, self.index):
                print(self.lines[i])
            print('_' * line_width, '\n')

            question = Question(lines=self.lines, index=self.index)
            question.execute()
            self.enabled = question.ask()
            if self.enabled:
                self.index += 1
                if question.answeredCorrectly():
                    print(random.choice(self.statements['correct']))
                    self.correct += 1
                else:
                    print(random.choice(self.statements['wrong']))
                anyKeyContinue()

                if self.index == len(self.lines):
                    print('\n---Complete---\n')
                    percent = f'{int(self.correct / len(self.lines) * 100)}'
                    print(f'{self.correct}/{len(self.lines)} {percent}%')
                    self.enabled = False

        print('\nGood bye\n')


def clearScreen():
    os.system('clear')


def anyKeyContinue():
    input('\nany key to continue')


if __name__ == '__main__':
    print(sys.argv)
    if(len(sys.argv) < 2):
        print('please call with a .txt file argument')
    else:
        app = App(sys.argv[1])
        app.run()
