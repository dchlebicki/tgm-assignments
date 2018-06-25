import abc


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def clock(self):
        pass