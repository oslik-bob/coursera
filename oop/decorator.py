from abc import ABC, abstractmethod


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