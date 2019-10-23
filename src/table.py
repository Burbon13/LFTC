class Table:
    def __init__(self):
        self.__array = {}

    def put(self, pos, value):
        self.__array[pos] = value

    def get(self, pos):
        return self.__array[pos]

    def has(self, pos):
        return pos in self.__array

    def get_all(self):
        return self.__array.values()

    def get_len(self):
        return len(self.__array)

    def append(self, value):
        if value not in self.__array:
            self.__array[value] = len(self.__array) + 1
        else:
            raise Exception('Value ' + value + ' already exists in table')

    def __str__(self):
        return str(self.__array)
