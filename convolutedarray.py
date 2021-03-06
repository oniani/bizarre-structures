"""
This module implements the Convoluted Array data structure.
It is rather interesting than useful data structure.
P.S. It does have some limited uses :)
"""


class ConvolutedArray:
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, idx):
        return self._items[idx]

    def __eq__(self, other):
        return self._items == other._items

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        out = "ConvolutedArray(["

        if self.is_empty():
            return out + "])"

        elif len(self._items) == 1:
            return out + str(self._items[0]) + "])"

        elif len(self._items) == 2:
            return "{}{}, {}])".format(out, self._items[0], self._items[1])

        elif len(self._items) % 2 == 0:
            for i in range(len(self._items)):
                if i < len(self._items) // 2 - 1:
                    out += "{}, [".format(self._items[i])
                elif i == len(self._items) // 2 - 1:
                    out += "{}, ".format(self._items[i])
                elif i == len(self._items) // 2:
                    out += "{}], ".format(self._items[i])
                elif i < len(self._items) - 1:
                    out += "{}], ".format(self._items[i])
                else:
                    out += "{}])".format(self._items[i])
        else:
            for i in range(len(self._items)):
                if i < len(self._items) // 2:
                    out += "{}, [".format(self._items[i])
                elif i == len(self._items) // 2:
                    out += "{}], ".format(self._items[i])
                elif i < len(self._items) - 1:
                    out += "{}], ".format(self._items[i])
                else:
                    out += "{}])".format(self._items[i])
        return out

    def get_pair(self, idx):
        """Get the pairs out of the Convoluted Array.

        Example:

            For instance, if the cnvarr = ConvolutedArray(1, 2, 3),
            cnvarr.get_pair(0) is [1, 3] and cnvarr.get_pair(1) is [2].
        """
        if len(self._items) % 2 == 0:
            return [self._items[idx], self._items[-1 - idx]]
        else:
            if idx == len(self._items) // 2:
                return [idx]
            else:
                return [self._items[idx], self._items[-1 - idx]]

    def flatten(self):
        """Flatten the Convoluted Array.

        For instance, if the cnvarr = ConvolutedArray(1, 2, 3),
        cnvarr.flatten() = [1, 2, 3].
        """
        return "ConvolutedArray({})".format(self._items)

    def clear(self):
        """Clear the Convoluted Array."""
        self._items = []

    def is_empty(self):
        """Check if the Convoluted Array is empty."""
        return self._items == []


def main():
    """Testing ConvolutedArray datatype"""
    # Testing Dupeless Stack creation
    cnvarr = ConvolutedArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    if cnvarr:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Testing magic method '__len__'
    if len(cnvarr) == 10:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing magic method '__repr__'
    if (
        str(cnvarr)
        == "ConvolutedArray([0, [1, [2, [3, [4, 5], 6], 7], 8], 9])"
    ):
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing method 'get_pair'
    if cnvarr.get_pair(1) == [1, 8]:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Testing method 'flatten'
    if cnvarr.flatten() == "ConvolutedArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])":
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Testing method 'clear'
    cnvarr.clear()
    if cnvarr == ConvolutedArray([]):
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Testing method 'is_empty'
    if cnvarr.is_empty():
        print("Test 6 passed")
    else:
        print("Test 6 failed")


if __name__ == "__main__":
    main()
