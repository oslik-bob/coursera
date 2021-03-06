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
         "Strength": +7,  # ????????
         "Perception": -3,  # ????????????????????
         "Endurance": +7,  # ????????????????????????
         "Charisma": -3,  # ??????????????
         "Intelligence": -3,  # ??????????????????
         "Agility": +7,  # ???????????????? 
         "Luck": +7  # ??????????
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
        "Strength": 2,  # ????????
        "Perception": 2,  # ????????????????????
        "Endurance": 2,  # ????????????????????????
        "Charisma": 2,  # ??????????????
        "Intelligence": 2,  # ??????????????????
        "Agility": 2,  # ???????????????? 
        "Luck": 2  # ??????????
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
        "Strength": -4,  # ????????
        "Endurance": -4,  # ????????????????????????
        "Agility": -4,  # ???????????????? 
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
        "Luck": -10  # ??????????
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
        "Strength": -2,  # ????????
        "Perception": -2,  # ????????????????????
        "Endurance": -2,  # ????????????????????????
        "Charisma": -2,  # ??????????????
        "Intelligence": -2,  # ??????????????????
        "Agility": -2,  # ???????????????? 
        "Luck": -2  # ??????????
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