#! /usr/bin/python
# ------------------------------------------------------------#
# Console quiz applicatoin where you get asked a series       #
# of mulitple choice questions on the given text file         #
# ------------------------------------------------------------#

import sys
import os
import random
from core.question import Question
from core.pretty_printer import PrettyPrint
from utils.input_helpers import wait_for_anykey, clear


__author__ = "Paul Lombard"
__version__ = "0.0.1"
__title__ = "Memorite"


class App:
    def __init__(self, text_file, no_shown_lines=4):
        self.enabled = True
        self.no_shown_lines = no_shown_lines
        self.text_file = text_file
        self.lines = None
        self.printer = None
        self.index = 0
        self.correct_count = 0

    def _extract_lines(self):
        '''Split text file into lines'''
        raw_text = ''
        with open(self.text_file, 'r') as f:
            raw_text = f.read()
        self.lines = raw_text.split('\n')

    def run(self):
        '''Runs app on the provided file'''
        self._extract_lines()
        self.printer = PrettyPrint(self.lines)

        while(self.enabled):
            clear()
            self.printer.header(self.correct_count, self.index)

            question = Question(
                lines=self.lines,
                index=self.index,
                printer=self.printer)
            self.enabled = question.ask()

            if self.enabled:
                self.index += 1
                if question.answered_correctly():
                    self.correct_count += 1
                self.printer.answer_statement(question.answered_correctly())

                wait_for_anykey()

                if self.index == len(self.lines):
                    self.printer.debrief(self.correct_count)
                    self.enabled = False

            else:
                self.printer.leave()


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print('Please call with a .txt file argument')
    else:
        app = App(sys.argv[1])
        app.run()
