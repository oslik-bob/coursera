import os
from posixpath import split
from tempfile import gettempdir

class File:
    def __init__(self, file_name) -> None:
        self.file_name=file_name
        if not os.path.exists(self.file_name):
            self.write('')

    def read(self):
        with open(self.file_name,'r') as f:
            return f.read()

    def write(self,new_str):
        """Принимает строку для записи в файл"""
        with open(self.file_name,'w') as f:
            f.write(new_str)
            return len(new_str)

    def __str__(self) -> str:
        if self:
            return os.path.realpath(self.file_name)
    
    def get_hash(self,obj1:classmethod,obj2:classmethod):
        result=''
        for i in (obj1, obj2):
            result+=hex(i.__hash__()).split('x')[1]
        return result

    def __add__(self, other):
        temp_file=os.path.join(gettempdir(),self.get_hash(self,other))
        with open(temp_file,'w') as tf:
            tf.write(self.read()+(other.read()))
        temp_file=File(temp_file)
        return temp_file

    def __iter__(self):
        with open(self.file_name,'r') as f:
            return iter(f.readlines())


"""import os
import uuid


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line"""