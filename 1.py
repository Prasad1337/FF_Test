# Imports
from collections import Counter


# Class of Items
class Items:
    __itemList = []

    # Constructor
    def __init__(self, item_list):
        self.__itemList = item_list

    def set_list(self, item_list):
        self.__itemList = item_list

    def get_list(self):
        return self.__itemList

    def get_unique_items(self):
        return set(self.__itemList)

    def get_items_with_frequencies(self):
        return Counter(self.__itemList)

    def add_item(self, item):
        self.__itemList.append(item)
