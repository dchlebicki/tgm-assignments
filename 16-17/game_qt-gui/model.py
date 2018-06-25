class Model:
    """
    Model part of the MVC pattern
    """
    def __init__(self):
        """
        Holds data/values and properties

        :ivar offen: int
        :ivar korrekt: int
        :ivar falsch: int
        :ivar gesamt: int
        :ivar spiele: int
        :ivar rows: int
        :ivar cols: int
        """
        self.offen = 0
        self.korrekt = 0
        self.falsch = 0
        self.gesamt = 0
        self.spiele = -1

        self.current_number = 1

        self.time = 0.0

        # number of rows/columns of the button grid
        self.rows = 3
        self.cols = 5


