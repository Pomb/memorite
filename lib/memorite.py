#! /usr/bin/python
import sys
import os
import random
import core.line_splitter as line_splitter
from core.printer import Printer
from core.settings import questions as settings
from core.quest_track import QuestTrack
from utils.helpers import wait_for_anykey, clear


class App:
    def __init__(self, text_file, **kargs):
        self.enabled = True
        self.text_file = text_file
        self.printer = Printer()
        self.lines = line_splitter.extract(text_file)
        self.quest_track = QuestTrack(
            lines=self.lines,
            num_options=kargs['options'],
            num_shown_lines=kargs['lines'])

    def run(self):
        '''The core loop of the application'''
        while(self.enabled):
            clear()

            if self.quest_track.complete:
                self.quest_track.debrief()
                self.enabled = False
                break
            elif self.quest_track.next():
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
            app = App(
                text_file=sys.argv[1],
                lines=lines,
                options=options)
            app.run()
    except Exception as e:
        print(e)
