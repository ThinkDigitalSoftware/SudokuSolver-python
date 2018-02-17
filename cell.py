class PossibleValues(list):
    is_already_set = False

    def append(self, value):

        """

        :param value: the value to add to the list
        :return: success if the value is added
        """
        if self.is_already_set:
            pass
        if hasattr(value, '__iter__'):  # If it's a list, then
            for item in value:  # for every item in the list
                if item not in self:  # If we already have this, don't add it again.
                    if self.__len__() < 9:
                        super().append(item)
                    else:
                        raise IndexError("This is putting us over 9!")
        elif self.__len__() < 9 and value not in self:
            super().append(value)
        else:
            raise IndexError("This is putting us over 9!")
        self.is_already_set = True
        return True


class Cell:
    possible_values = PossibleValues()

    def __init__(self, row, column, value=0, box=0):
        self.row = row
        self.column = column
        self.value = int(value)
        self.box = box

    def __eq__(self, other):
        if isinstance(other, int):
            # print("eq == {0}".format(self.value == Cell(0, 0, other).value))
            return self.value == Cell(0, 0, other).value
        else:
            return True

    def __ne__(self, other):
        # print("__ne__: {0}".format(self.value != other))
        return self.value != other

    def __radd__(self, other):
        return self.value + other

    def __repr__(self):
        return str(self.value)

    def set(self, value):
        self.value = int(value)

    def to_int(self):
        return self.value
