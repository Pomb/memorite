class ScoreKeeper:
    def __init__(self, total):
        self.total = total
        self.index = 0
        self.correct = 0

    @property
    def complete(self):
        return self.index == self.total

    @property
    def percent(self):
        return int(self.correct / self.total) * 100

    @property
    def out_of(self):
        return f'{self.correct}/{self.total}'

    def add_score(self, correct):
        self.index += 1
        if correct:
            self.correct += 1
