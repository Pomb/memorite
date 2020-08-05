#! /usr/bin/python
# ------------------------------------------------------------#
# Console quiz application where you get asked a series       #
# of mulitple choice questions on the given text file         #
# ------------------------------------------------------------#

import sys
import os
import random
from lib.core.question import Question
from lib.core.pretty_printer import PrettyPrint
from lib.core.settings import questions as settings
import lib.core.line_splitter as line_splitter
from lib.core.score_keeper import ScoreKeeper
from lib.utils.input_helpers import wait_for_anykey, clear


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
        self.lines = line_splitter.extract(text_file)
        self.printer = PrettyPrint()
        self.score_keeper = ScoreKeeper(len(self.lines))

    def _create_new_question(self):
        return Question(
            lines=self.lines,
            index=self.score_keeper.index,
            printer=self.printer,
            num_options=self.num_options,
            num_shown_lines=self.num_shown_lines)

    def run(self):
        '''The core loop of the application'''
        while(self.enabled):
            clear()

            if self.score_keeper.complete:
                self.printer.debrief(self.score_keeper)
                self.printer.lines(self.lines)
                self.enabled = False
                break

            self.printer.header(self.score_keeper)
            question = self._create_new_question()

            if question.ask():
                is_correct = question.answered_correctly()
                self.score_keeper.add_score(is_correct)
                self.printer.answer_statement(is_correct)
                wait_for_anykey()
            else:
                self.printer.leave()
                break


if __name__ == '__main__':
    try:
        # user defined number of lines shown
        lines = int(sys.argv[2])
        # user defined number of answer options
        options = int(sys.argv[3])
    except:
        # use defaults if none are provided
        lines = settings['number_show_lines']
        options = settings['number_of_options']
        pass

    try:
        if len(sys.argv) < 2:
            raise Exception('Error! Please provide a .txt file path argument')
        else:
            app = App(text_file=sys.argv[1], lines=lines, options=options)
            app.run()
    except Exception as e:
        print(e)
