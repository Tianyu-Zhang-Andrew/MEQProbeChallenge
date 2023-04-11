
class Node:
    def __init__(self, value):
        self.__value = value
        # self.__neighbors = []
        self.__explored_count = 0

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    # def has_neighbor(self, neighbor_value):
    #     for neighbor in self.__neighbors:
    #         if neighbor.get_value() == neighbor_value:
    #             return True
    #
    #     return False

    # def add_neighbor(self, neighbor):
    #     self.__neighbors.append(neighbor)
    #
    # def set_neighbors(self, neighbors):
    #     self.__neighbors = neighbors
    #
    # def get_neighbors(self):
    #     return self.__neighbors

    def get_explored_count(self):
        return self.__explored_count

    def set_explored_count(self, explored_count):
        self.__explored_count = explored_count
