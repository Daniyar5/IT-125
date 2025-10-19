class Account():
    def __init__(self, name, pin, number, balance):
        self.name = name
        self.__pin = pin
        self.__number = number
        self.__balance = balance

    def deposit(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                self.__balance += amount
        else:
            return 'Неверный пин'

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                return 'На вашем балансе не достаточно средств'
        else:
            return 'Неверный пин'

    def get_balance(self, pin):
        if pin == self.__pin:
            return f'Ваш баланс: {self.__balance}'
        else:
            return 'Неверный пин'

acc = Account('Дани', "1234", "0022", 1000)
# print(acc.name)

# print(acc.deposit(200, "1234"))
# print(acc.withdraw(230, "1234"))
# print(acc.get_balance('1234'))





class Product():
    def __init__(self, price):
        self.__price = price
    
    def set_discount(self, percent):
        if 0 < self.__price >= percent:
            self.__price = percent / 100 * self.__price - self.__price
            self.__price *= -1
        else:
            return 'Достиг лимин скидки'
        
    def final_price(self):
        return f"Ваша итоговая цена: {self.__price}"
        
prod = Product(100)
# print(prod.set_discount(20))
# print(prod.final_price())





class Course():
    def __init__(self, title, student, maxSeats):
        self.__title = title
        self.__student = student
        self.__maxSeats = maxSeats

    def add_student(self, name):
        if len(self.__student) < self.__maxSeats:
            self.__student.append(name)
        else:
            return 'Нет мест'
        
    def remove_student(self, name):
        self.__student.remove(name)

    def get_students(self):
        return f'Список студентов куса {self.__title}:\n{self.__student}'

students = [
    'Данияр', "Иван", "Мирсалим", "Улан",
    "Адилет", "Григорий", "Мадина", "Саша"
]

course = Course('Матем', students, 10)
# print(course.add_student('Лиза'))
# print(course.remove_student('Улан'))
# print(course.get_students())





class SmartWatch():
    def __init__(self, battery):
        self.__battery = battery

    def use(self, minutes):
        if minutes >= 10:
            self.__battery -= 1
        
    def charge(self, percent):
        if self.__battery < 100:
            self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100

    def get_battery(self):
        return f'Уровень заряда: {self.__battery}'
    
phone = SmartWatch(60)
# print(phone.use(11))
# print(phone.charge(30))
# print(phone.get_battery())





class Transport():
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        time = distance / self.speed
        return f'Время поездки: {time} ч'
    
class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)
    
    def travel_time(self, distance):
        return super().travel_time(distance)
    
class  Train(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def travel_time(sefl, distance):
        return super().travel_time(distance)
    
class Airplane(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)
    
    def travel_time(self, distance):
        time = distance / self.speed
        time *= 0.8
        return f'Время поездки: {time} ч'
        
bus = Bus(5, 30)
train = Train(10, 400)
airplane = Airplane(20, 200)
# print(bus.travel_time(20))
# print(train.travel_time(30))
# print(airplane.travel_time(100))






class Order():
    def calculate_total(self):
        return f''

class DineInOrder(Order):
    def calculate_total(self):
        return super().calculate_total() + f'заказ обеда'
    
class TakeAwayOrder(Order):
    def calculate_total(self):
        return super().calculate_total() + f'взять с собой'

class DeliveryOrder(Order):
    def calculate_total(self):
        return super().calculate_total() + f'Доставка + 10% к стоимости'

    






class Character():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def Attack(self):
        return f'{self.name}: '

class Warrior(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def Attack(self):
        return super().Attack() + f'бьёт мечом'
    
class Mage(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def Attack(self):
        return super().Attack() + f'атакует магией'
    
class Archer(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
    
    def Attack(self):
        return super().Attack() + f'стреляет из лука'
    
warrior = Warrior('Валодя', 100, 10)
mage = Mage('Светлана', 60, 20)
arher = Archer('Виктор', 80, 5)
# print(warrior.Attack())
# print(mage.Attack())
# print(arher.Attack())






class MediaFile():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class AudioFile(MediaFile):
    def __init__(self, title, duration):
        super().__init__(title, duration)

    def play(self):
        return f'воспроизводится с аудио'
    
class VideoFile(MediaFile):
    def __init__(self, title, duration):
        super().__init__(title, duration)
    
    def play(self):
        return f'воспроизводится c видео'

class Podcast(MediaFile):
    def __init__(self, title, duration):
        super().__init__(title, duration)

    def play(self):
        return f'воспроизводится подкаст'
    



class PaymentSystem():
    def process_payment(self, amount):
        return f'{amount}'

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        return super().process_payment(amount) + f'сомов оплачено'
    
class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return super().process_payment(amount) + f'биткойнов оплачено'
    
class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        return super().process_payment(amount) + f'сомов переведено'

    





class Animal():
    def __init__(self, title):
        self.title = title
    
    def eat(self):
        return f'{self.title}: ест '
    
    def sleep(self):
        return f'{self.title}: спит '
    
class Lion(Animal):
    def __init__(self, title):
        super().__init__(title)

    def eat(self):
        return super().eat() + f'мясо'
    
    def sleep(self):
        return super().sleep() + f'уложившись на бок'
    
class Elephant(Animal):
    def __init__(self, title):
        super().__init__(title)

    def eat(self):
        return super().eat() + f'траву'
    
    def sleep(self):
        return super().sleep() + f'уложившись на бок'
    
class Snake(Animal):
    def __init__(self, title):
        super().__init__(title)

    def eat(self):
        return super().eat() + f'мясо'
    
    def sleep(self):
        return super().sleep() + f'свернувшись'
    
lion = Lion('Лев')
# print(lion.eat())
# print(lion.sleep())








class Document():
    def open(self):
        return f'Открытие '
    def edit(self):
        return f'Редактирование '
    def save(self):
        return f'Сохранение '
    
class WordDocument(Document):
    def open(self):
        return super().open() + f'ворд документа'
    def edit(self):
        return super().edit() + f'ворд документа'
    def save(self):
        return super().save() + f'ворд документа'
    
class PdfDocument(Document):
    def open(self):
        return super().open() + f'Pdf документа'
    def edit(self):
        return super().edit() + f'Pdf документа'
    def save(self):
        return super().save() + f'Pdf документа'
    
class SpreadsheetDocument(Document):
    def open(self):
        return super().open() + f'Табличного документа'
    def edit(self):
        return super().edit() + f'Табличного документа'
    def save(self):
        return super().save() + f'Табличного документа'






class Lesson():
    def start(self):
        return f'Начало '
    
class VideoLesson(Lesson):
    def start(self):
        return super().start() + f'видео урока'
    
class QuizLesson(Lesson):
    def start(self):
        return super().start() + f'контрольной'
    
class TextLesson(Lesson):
    def start(self):
        return super().start() + f'текстового урока'
    





class EmailNotification():
    def send(self, message):
        return f'Сообщение по Email: {message}'
    
class SMSNotification():
    def send(self, message):
        return f'Сообщение по SMS: {message}'
    
class PushNotification():
    def send(self, message):
        return f'Push уведомление: {message}'
    

user_1 = EmailNotification()
# print(user_1.send('Привет бедолага'))





class Square():
    def perimeter(self, sides):
        sides *= 4
        return f'Перемитр квадрата равен: {sides}'
    
class Triangle():
    def perimeter(self, side_1, side_2, side_3):
        return f'Перемитр теругольника равен: {side_1 + side_2 + side_3}'
    
class Circle():
    def perimeter(self, diameter):
        return f'Перемитр круга равен: {3.14 * diameter}'
    
square = Square()
triangle = Triangle()
circle = Circle()

figures = [
    square.perimeter(2), triangle.perimeter(3,3,6), circle.perimeter(4)
]

for figure in figures:
    print(f'{figure}')







class Manager():
    def work(self):
        return f'Выполняет работу менджера'
    
class Developer():
    def work(self):
        return f'Разрабатывает что-то'
    
class Designer():
    def work(self):
        return f'Придумывает дизайн'
    






class FireSpell():
    def cast(self, target):
        return f'Наносит урон огнём по {target}'
    
class IceSpell():
    def cast(self, target):
        return f'Наносит урон заморозкой по {target}'
    
class HealingSpell():
    def cast(self, target):
        return f'Востанавливает здоровье {target}'