from collections import Counter

class Items:
    __itemList = []

    def __init__(self, itemList):
        self.__itemList = itemList

    def setList(self, itemList):
        self.__itemList = itemList

    def getList(self):
        return self.__itemList

    def getUniqueItems(self):
        return set(self.__itemList)

    def getItemsWithFrequencies(self):
        return Counter(self.__itemList)

    def addItem(self, item):
        self.__itemList.append(item)
