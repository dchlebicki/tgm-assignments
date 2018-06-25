class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def clock(self):
        self._strategy.clock()