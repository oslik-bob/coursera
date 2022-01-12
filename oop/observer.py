#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 15:46:35 2022

@author: kali


Наблюдатель

"""

from abc import abstractmethod, ABC


class AbstractObserver(ABC):
    """
    АБС класс
    """

    @abstractmethod
    def update(self, dick):
        """абс функция"""
        pass


#class ObservableEngine(Engine): # для задания
class ObservableEngine():
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class ShortNotificationPrinter(AbstractObserver):
    """
    атрибуте achievements
    хранится множество названий полученных достижений

    """
    def __init__(self):
        self.achievements = set()

    def update(self, dick:dict):
        #self.achievements.add(dick['title']) # для задания
        if type(dick['title']) in (str, int):
            self.achievements.add(str(dick['title']))
        else:
            for i in dick['title']:
                self.achievements.add(str(i))


class FullNotificationPrinter(AbstractObserver):
    """
    список достижений в том порядке,
    в котором они генерируются Engine
    """
    def __init__(self):
        self.achievements = list()

    def update(self, dick:dict):
        #self.achievements.append(dick) # для задания
        if type(dick['text']) in (str, int):
            if dick['text'] not in self.achievements:
                self.achievements.append(dick['text'])
        else:
            for i in dick['text']:
                if i not in self.achievements:
                    self.achievements.append(i)

# =============================================================================
#
# if __name__=='__main__':
#     full1=FullNotificationPrinter()
#     short1=ShortNotificationPrinter()
#     man=ObservableEngine()
#     man.subscribe(short1)
#     man.subscribe(full1)
#     man.notify({
#         "title":
#             ["Покоритель",
#              'fg'],
#         "text":
#             ["Дается при выполнении всех заданий в игре",
#              "1 всех заданий в игре",
#              "2",
#              "3"]})
# =============================================================================
