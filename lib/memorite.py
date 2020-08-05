#! /usr/bin/python
# ------------------------------------------------------------#
# Console quiz application where you get asked a series       #
# of mulitple choice questions on the given text file         #
# ------------------------------------------------------------#

import sys
import os
import random
from core.question import Question
from core.pretty_printer import PrettyPrint
from core.settings import questions as settings
from utils.input_helpers import wait_for_anykey, clear
import core.line_splitter as line_splitter


__author__ = "Paul Lombard"
__version__ = "0.0.1"
__title__ = "Memorite"


class App:
    def __init__(self, text_file, **kargs):
        print(kargs)
        self.enabled = True
        self.num_shown_lines = kargs['lines']
        self.num_options = kargs['options']
        self.text_file = text_file
        self.lines = None
        self.printer = None
        self.index = 0
        self.correct_count = 0

    @property
    def _complete(self):
        return self.index == len(self.lines)

    def _create_new_question(self):
        return Question(
            lines=self.lines,
            index=self.index,
            printer=self.printer,
            num_options=self.num_options,
            num_shown_lines=self.num_shown_lines)

    def run(self):
        '''The core loop of the application'''
        self.lines = line_splitter.extract(self.text_file)
        self.printer = PrettyPrint(self.lines)

        while(self.enabled):
            clear()
            self.printer.header(
                correct=self.correct_count,
                index=self.index)

            question = self._create_new_question()

            if question.ask():
                self.index += 1
                if question.answered_correctly():
                    self.correct_count += 1
                self.printer.answer_statement(question.answered_correctly())

                wait_for_anykey()

                if self._complete:
                    clear()
                    self.printer.debrief(self.correct_count)
                    self.printer.full_text()
                    self.enabled = False

            else:
                self.printer.leave()
                break


if __name__ == '__main__':
    text_file = sys.argv[1]
    lines = settings['number_show_lines']
    options = settings['number_of_options']
    try:
        lines = int(sys.argv[2])
        options = int(sys.argv[3])
    except IndexError:
        print('using defaults')

    if text_file is None:
        print('Please call with a .txt file argument')
    else:
        app = App(
            text_file=text_file,
            lines=lines,
            options=options)
        app.run()
