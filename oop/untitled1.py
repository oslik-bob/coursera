#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:10:38 2022

@author: kali
"""
# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()
    
  
# =============================================================================
# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
# 
#         self.stats = {
#             "HP": 128,
#             "MP": 42,
#             "SP": 100,
# 
#             "Strength": 15,
#             "Perception": 4,
#             "Endurance": 8,
#             "Charisma": 2,
#             "Intelligence": 3,
#             "Agility": 8,
#             "Luck": 1
#         }
# 
#     def get_positive_effects(self):
#         return self.positive_effects.copy()
# 
#     def get_negative_effects(self):
#         return self.negative_effects.copy()
# 
#     def get_stats(self):
#         return self.stats.copy()
#    
# =============================================================================
  
class AbstractEffect(ABC, Hero):
    
    def __init__(self, base):
        self.base = base
        
    @abstractmethod    
    def get_positive_effects(self):
        self.base.get_positive_effects()
        
    @abstractmethod  
    def get_negative_effects(self):
         self.base.get_negative_effects()
    @abstractmethod  
    
    def get_stats(self):
        self.base.get_stats()
    
    
class AbstractPositive(AbstractEffect):
    
    def __init__(self, base):
        self.base = base
        
    @abstractmethod    
    def get_positive_effects(self):
        self.base.get_positive_effects()
    @abstractmethod  
    def get_negative_effects(self):
         self.base.get_negative_effects()
    @abstractmethod  
    def get_stats(self):
        self.base.get_stats()
           
    
class AbstractNegative(AbstractEffect):
    
    def __init__(self, base):
        self.base = base
        
    @abstractmethod    
    def get_positive_effects(self):
        self.base.get_positive_effects()
    @abstractmethod  
    def get_negative_effects(self):
         self.base.get_negative_effects()
    @abstractmethod  
    def get_stats(self):
        self.base.get_stats()


class Berserk(AbstractPositive):

    negative_effects = []
    positive_effects = ['Berserk']
    stats = {
         "HP": +50,  # health points
         "Strength": +7,  # сила
         "Perception": -3,  # восприятие
         "Endurance": +7,  # выносливость
         "Charisma": -3,  # харизма
         "Intelligence": -3,  # интеллект
         "Agility": +7,  # ловкость 
         "Luck": +7  # удача
         }
        
    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects 
         
    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects
    
    def get_stats(self):
        a = self.base.get_stats()
        for i in self.stats:
            a[i]+=self.stats[i]
        return a
        
        
class Blessing(AbstractPositive):

    negative_effects = []
    positive_effects = ['Blessing']
    stats = {
        "Strength": 2,  # сила
        "Perception": 2,  # восприятие
        "Endurance": 2,  # выносливость
        "Charisma": 2,  # харизма
        "Intelligence": 2,  # интеллект
        "Agility": 2,  # ловкость 
        "Luck": 2  # удача
        }
    
    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects 
         
    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects
        
    def get_stats(self):
        a = self.base.get_stats()
        for i in self.stats:
            a[i]+=self.stats[i]
        return a
    

class Weakness(AbstractNegative):

    positive_effects = []
    negative_effects = ['Weakness']
    stats = {
        "Strength": -4,  # сила
        "Endurance": -4,  # выносливость
        "Agility": -4,  # ловкость 
        }

    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects 
         
    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects
    
    def get_stats(self):
        a = self.base.get_stats()
        for i in self.stats:
            a[i]+=self.stats[i]
        return a 
        
        
class EvilEye(AbstractNegative):

    positive_effects = []
    negative_effects = ['EvilEye']
    stats = {
        "Luck": -10  # удача
        }

    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects 
         
    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects
    
    def get_stats(self):
        a = self.base.get_stats()
        for i in self.stats:
            a[i]+=self.stats[i]
        return a
  
        
class Curse(AbstractNegative):


    positive_effects = []
    negative_effects = ['Curse']
    stats = {
        "Strength": -2,  # сила
        "Perception": -2,  # восприятие
        "Endurance": -2,  # выносливость
        "Charisma": -2,  # харизма
        "Intelligence": -2,  # интеллект
        "Agility": -2,  # ловкость 
        "Luck": -2  # удача
        }
        
    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects 
         
    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects
        
    
    def get_stats(self):
        a = self.base.get_stats()
        for i in self.stats:
            a[i]+=self.stats[i]
        return a

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    print(cur1.get_positive_effects())
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')