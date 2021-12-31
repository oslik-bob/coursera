import csv
from os import read, path

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if not all ((
            brand,
            photo_file_name,
            carrying
        )):
            raise ValueError
        else:    
            self.brand=brand 
            self.photo_file_name=photo_file_name
            self.carrying=float(carrying)
            self._chk=self.get_photo_file_ext()


    def get_photo_file_ext(self):
        _, a=path.splitext(self.photo_file_name)
        if a in ['.jpg', '.jpeg', '.png', '.gif']:
            return path.splitext(self.photo_file_name)[1]
        else:
            raise ValueError


class Car(CarBase):

    """#
    # 
    #  БАЗОВЫЙ КЛАСС
    #
    #"""
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count,car_type=None):
        #self._check=self.check()
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.passenger_seats_count=int(passenger_seats_count)
        self.car_type='car'


class Truck(CarBase):
    """#
    # 
    # ГРУЗОВИК
    #
    #"""
    def __init__(self, brand, photo_file_name, carrying, body_whl, car_type=None):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.body_whl=body_whl
        self.car_type="truck"
        self.body_length, self.body_width, self.body_height=self.lwh_split(body_whl)


    def lwh_split(self,lwh:str)-> list:
        result=[]
        if len(lwh.split('x'))!=3:
            return [0.0, 0.0, 0.0]
        else:
            for i in range(3):
                try:
                    result.append(float(lwh.split('x')[i]))
                except (ValueError,IndexError):
                    return [0.0, 0.0, 0.0]
            return result


    def get_body_volume(self):
        return self.body_height*self.body_width*self.body_length


class SpecMachine(CarBase):
    """#
    # 
    # спец транспорт
    #
    #"""
    def __init__(self, brand, photo_file_name, carrying, extra, car_type=None):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        if extra:
            self.extra=extra
        else:
            raise ValueError
        self.car_type='spec_machine'      


def get_car_list(csv_filename):
    car_list=iter(open_csv_file(csv_filename))
    result=[]
    try:
        next(car_list)
        while True:
            a=next(car_list)
            if 'car' in a:
                try:
                    result.append(Car(brand=a[1],
                    passenger_seats_count=a[2],
                    photo_file_name=a[3],
                    carrying=a[5]))
                except (ValueError, IndexError):
                    pass

            elif 'spec_machine' in a:
                try:
                    result.append(SpecMachine(brand=a[1],
                    photo_file_name=a[3],
                    carrying=a[5],
                    extra=a[6]))
                except (ValueError, IndexError):
                    pass
                    
            elif 'truck' in a:
                try:
                    result.append(Truck(brand=a[1],
                    photo_file_name=a[3],
                    body_whl=a[4],
                    carrying=a[5])) 
                except (ValueError, IndexError):
                    pass   
    except StopIteration:
        pass
    return result

def open_csv_file(dir_file):
    try:    
        with open(dir_file) as csv_fd:
            reader = csv.reader(csv_fd,delimiter=";")
            s=([r for r in reader])
            return s
    except IOError:
        pass