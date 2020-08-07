from enum import Enum
import random
from core.question.choose_line import ChooseLine
from core.question.choose_word import ChooseWord


class QuestionType(Enum):
    ChooseLine = 0,
    ChooseWord = 1,
    # SortLines = 2,
    # TypeWord = 3,
    # TypeLine = 4


class QuestionFactory:
    def __init__(self, lines, num_options, num_shown_lines):
        self.lines = lines
        self.num_options = num_options
        self.num_shown_lines = num_shown_lines

    def next(self, index):
        q_type = random.choice(list(QuestionType))
        print(q_type, '\n')
        if(q_type == QuestionType.ChooseLine):
            question = ChooseLine(
                lines=self.lines,
                index=index,
                num_options=self.num_options,
                num_shown_lines=self.num_shown_lines)
        elif(q_type == QuestionType.ChooseWord):
            question = ChooseLine(
                lines=self.lines,
                index=index,
                num_options=self.num_options,
                num_shown_lines=self.num_shown_lines)
        else:
            raise ValueError(f'{q_type} is not a supported question type')

        question.execute()
        return question
