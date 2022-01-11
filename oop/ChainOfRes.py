
'''
Необходимо реализовать поведение:
EventGet(<type>) создаёт событие получения данных соответствующего типа
EventSet(<value>) создаёт событие изменения поля типа type(<value>)
Необходимо реализовать классы NullHandler, IntHandler, FloatHandler, StrHandler
так, чтобы можно было создать цепочку:
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

Описание работы цепочки:  

    chain.handle(obj, EventGet(int)) — вернуть значение obj.integer_field

    chain.handle(obj, EventGet(str)) — вернуть значение obj.string_field

    chain.handle(obj, EventGet(float)) — вернуть значение obj.float_field

    chain.handle(obj, EventSet(1)) — установить значение obj.integer_field =1

    chain.handle(obj, EventSet(1.1)) — установить значение obj.float_field = 1.1

    chain.handle(obj, EventSet("str")) — установить значение obj.string_field = "str"
'''
EVENT_INT, EVENT_FLOAT, EVENT_STR = "int", "float", "str"

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""
        

class Event_Get:
    
    def __init__(self, kind):
        self.kind = kind   


class Event_Set:
    
    def __init__(self, kind):
        self.kind = kind   


class NullHandler:        
    def __init__(self, success=None):
        self.__success = success

    def handle(self, char, event):
        if self.__successor is not None:
            self.__success.handle(char, event)


class IntHandler(NullHandler):
    pass


class FloatHandler(NullHandler):
    pass


class StrHandler (NullHandler):
    pass

class TypeGiver:
    
    def __init__(self):
        self.handlers = StrHandler
        (FloatHandler
        (IntHandler
        (NullHandler()
        )))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, char):
        for event in self.events:
            self.handlers.handle(char, event)
if __name__=='__main__':
    events=[]