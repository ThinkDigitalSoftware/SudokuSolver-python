class PossibleValues(list):
    def update(self, value):
        if self.__len__() < 9:
            self.update(value)
        else:
            raise IndexError
        return True


class Cell:
    possible_values = PossibleValues()

    def __init__(self, row, column, value=0):
        self.row = row
        self.column = column
        self.value = int(value)

    def __radd__(self, other):
        return self.value + other

    def __repr__(self):
        return str(self.value)

    def update(self, value):
        self.value = int(value)
        return
