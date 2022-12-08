import datetime as DT
def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate

class Car:
    # VIN-номер, марка, модель, год выпуска, мощность, пробег, кол-во владельцев, стоимость
    def __init__(self, VIN, old,  mark, model, year, power, km, amount, cost):
        self.VIN = VIN
        self.old = old
        self.mark = mark
        self.model = model
        self.year = int(year)
        self.power = int(power)
        self.km = int(km)
        self.amount = int(amount)
        self.cost = cost

    # вывод информации о текущем автомобиле
    def __str__(self):
        return f"{'VIN' if self.old=='б/у' else 'Госномер'}: {self.VIN}, марка: {self.mark}" \
               f" модель: {self.model}, год выпуска: {self.year}, мощность: {self.power}, лс, " \
               f" пробег: {self.km}, количество владельцев: {self.amount}, стоимость: {self.cost} млн. руб."
    # сумма налога
    def get_tax(self):
        if self.power < 100:
            tax=10
            sum_tax=self.power*tax
            return sum_tax
        elif self.power < 150:
            tax = 34
            sum_tax = self.power * tax
            return sum_tax
        else:
            tax = 49
            sum_tax = self.power * tax
            return sum_tax

    # увеличение пробега
    def set_mileage(self, kmr):
        self.km += kmr

    def get_age(self):
        current_date = DT.date.today().year
        return current_date - self.year

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

class Owner:
    # ФИО, номер в/у, дата рождения, область, автомобили
    def __init__(self, fio, vu,  burth_date, oblast, cars=None):
        self.fio = fio
        self.vu = int(vu)
        self.burth_date = burth_date
        self.oblast = oblast
        if cars is None:
            cars = list()
        self.cars = cars

    # Добавляем автомобиль владельцу
    def append(self, owner):
        self.cars.append(owner)

    # вывод информации о текущем владельце
    def __str__(self):
        return f" ФИО: {self.fio}, водительское удостоверение: {self.vu}" \
               f" дата рождения': {self.burth_date}, область, где выданы права: {self.oblast}," \
               f" автомобили: {self.cars}"

avto_1 = Car("О811КК750", "б/у", 'Renaught', 'Duster', 2015, 110, 27889, 3, 1.2)
print(avto_1)
print("Налог на мощность:", avto_1.get_tax())
print("Возраст:", avto_1.get_age())
avto_2 = Car("1KLBN52TWXM186109", "новая", 'Renaught', 'Duster', 2021, 130, 7889, 2, 1.7)
print(avto_2)
print("Налог на мощность:", avto_2.get_tax())
print("Возраст:", avto_2.get_age())
avto_3 = Car("1KLBN52TWXM186109", "новая", 'Renaught', 'Duster', 2022, 180, 7889, 2, 3.7)
print(avto_3)
print("Налог на мощность:", avto_3.get_tax())
print("Возраст:", avto_3.get_age())
avto_3.set_mileage(1000)
print(avto_3)
print(avto_1.get_age() < avto_2.get_age())
print(avto_1.get_age() > avto_3.get_age())
print(avto_3.get_age() != avto_2.get_age())

owner_1 = Owner('Кагарманов Родион Радикович', 1234567890, '12.12.1970', 'Момсковская', avto_1)
print(owner_1)
owner_1.append(avto_2)
print(owner_1)
