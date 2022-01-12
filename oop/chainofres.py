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


class SomeObject:
    """
    start objeckt
    """
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    """
    класс для получения данных из цепочки
    """
    def __init__(self, kind):
        self.kind = kind
        self.event = 'get'


class EventSet:
    """
    класс для передачи данных в цепочку
    """

    def __init__(self, kind):
        self.kind = kind
        self.event = 'set'


class NullHandler:
    """
    нулевая рука
    """
    def __init__(self, success = None):
        self.__success = success

    def handle(self, char, event):
        """
        перебираются цепочки... вроде
        """
        if self.__success is not None:
            return self.__success.handle(char, event)


class IntHandler(NullHandler):
    """
    ищем целое если нет идем дальше
    """
    def handle(self, char, event):
        if (event.event=="set" and isinstance(event.kind, int)):
            char.integer_field=event.kind

        elif (event.event=='get' and event.kind is int):
            return char.integer_field

        else:
            return super().handle(char, event)


class FloatHandler(NullHandler):
    """
    ищем флоат если нет идем дальше
    """
    def handle(self, char, event):
        if (event.event=="set" and isinstance(event.kind, float)):
            char.float_field=event.kind

        elif (event.event=='get' and event.kind is float):
            return char.float_field

        else:
            return super().handle(char, event)


class StrHandler (NullHandler):
    """
    ищем строку если нет идем дальше
    """
    def handle(self, char, event):
        if (event.event=="set" and isinstance(event.kind, str)):
            char.string_field=event.kind

        elif (event.event=='get' and event.kind is str):
            return char.string_field

        else:
            return super().handle(char, event)


if __name__=='__main__':
    obj = SomeObject()
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    obj.integer_field = 55
    obj.float_field = 0.5
    obj.string_field = 'some text'
    print(chain.handle(obj, EventGet(int)))
    chain.handle(obj, EventSet(45))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet(4.5))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
    print(obj.integer_field)
    print(obj.float_field)
    print(obj.string_field)
    