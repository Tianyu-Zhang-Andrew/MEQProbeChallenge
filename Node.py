
class Node:
    def __init__(self, value):
        self.__value = value
        self.__explored_count = 0

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_explored_count(self):
        return self.__explored_count

    def set_explored_count(self, explored_count):
        self.__explored_count = explored_count
