import random
from abc import ABC
from core.printer import Printer
from core.actions import Action


class Question(ABC):
    def __init__(self, lines, index):
        self.lines = lines
        self.index = index

    def display_question(self):
        pass

    def ask(self):
        return Action.Continue
