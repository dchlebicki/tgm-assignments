import datetime
import time

class Model:
    """
    Does all the data stuff
    """

    def get_time_tuple(self):
        """
        Returns the current time as a tuple in (hours, minutes, seconds, microseconds) form, fields of tuple are
        formatted e.g. hour: "09" instead of "9"
        :return: tuple
        """
        # ugly workaround because time.strftime doesn't support %f (milliseconds) on windows?
        now = datetime.datetime.now()
        return time.strftime("%H"), time.strftime("%M"), time.strftime("%S"), now.microsecond
