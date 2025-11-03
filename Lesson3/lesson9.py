class Payment():
    def __init__(self, balance):
        self.balance = balance

    def  pay(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            return f'Сумма оплаты {amount}'
        else:
            return f'Оплата не пройдена'

    def refund(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Возврать в сумме {amount}'
        else:
            return f'Возврать не удолся'
        

class  CreditCardPayment(Payment):
    def __init__(self, balance, limit):
        super().__init__(balance,)
        self.limit = limit

    def pay(self, amount):
        if amount > 0 and self.balance - amount > self.limit:
            self.balance -= amount
        else:
            return f'Вы достигли лимита'

    def refund(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Сумма {amount} возвращена'
        else:
            return f'Не удоалось вернуть сумму'
        


class CryptoPayment(Payment):
    def __init__(self, balance, pin):
        super().__init__(balance)
        self.__pin = pin

    def pay(self, amount, pin):
        if  pin == self.__pin:
            if amount > 0 and amount < self.balance:
                self.balance -= amount
                return f'Сумма оплаты криптой {amount}'
            else:
                return f'Оплата криптой не пройдена'
        else:
            return f'Неверный пинкод'
        
    def refund(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                self.balance += amount
                return f'Возврать в сумме {amount}'
            else:
                return f'Возврать не удолся'
        else:
            return f'Неверный пинкод'
        
# user = str(input('Выберите каким способом оплатить:\n1.Просто оплатить\n2.Кредиткой\n3.КриптоВалютой\n'))

# if user == '1':
#     BankAcc = Payment(1000)
#     print(BankAcc.pay(10))
#     print(f'Ваш баланс: {BankAcc.balance}')
# if user == '2':
#     BankAcc = CreditCardPayment(100, -300)
#     print(BankAcc.pay(200))
#     print(f'Ваш баланс: {BankAcc.balance}')
# if user == '3':
#     BankAcc = CryptoPayment(200, '1234')
#     pin = str(input('Введите пинкод: '))
#     print(BankAcc.pay(150, pin))
#     print(f'Ваш баланс: {BankAcc.balance}')









class Course():
    def start(self):
        return f'Начало занятий'

    def get_materials(self):
        return f'Лекция'

    def end(self):
        return f'Конец занятий'

class PythonCourse(Course):
    def start(self):
        return super().start() + f' по Python'
    
    def get_materials(self):
        return super().get_materials() + f' по теме Python'
    
    def end(self):
        return super().end() + f' по Python'
    
class MathCourse(Course):
    def start(self):
        return super().start() + f' по Математике'
    
    def get_materials(self):
        return super().get_materials() + f' по теме Математика'
    
    def end(self):
        return super().end() + f' по Математике'
    










class Delivery():
    def calculate_cost(self, distance):
        self.price *= distance

    def deliver(self):
        return f'Ваша даставка стоит: {self.price} сомов'

class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        self.price = 2
        return super().calculate_cost(distance)

    def deliver(self):
        return super().deliver()
    
class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        self.price = 3
        return super().calculate_cost(distance)
    
    def deliver(self):
        return super().deliver()
    
class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        self.price = 1
        return super().calculate_cost(distance)
    
    def deliver(self):
        return super().deliver()










class BankAccount():
    def __init__(self, owner, balance, pin):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                self.__balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount > 0:
                self.__balance += amount

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            new_pin = self.__pin

acc = BankAccount('Umembvaludaf', 1500, '12345')
print(acc.deposit(120, '12345'))
print(acc.withdraw(120, '12345'))
print(acc.change_pin('12345', '4321'))









class UserProfile():
    def __init__(self, email, password, status):
        self.__email = email
        self.__password = password
        self._status = status

    def login(self, email, password):
        if email == self.__email:
            if password == self.__password:
                return f'Вы успешно вошли'
            else:
                return f'Неверный пароль'
        else:
            return f'Неверный email'

    def upgrade_to_premium(self):
        self._status = 'Premium'
        return f'ООООоооооооооо у тебя теперь премиум'

    def get_info(self):
        return f'{self.__email}'

# accaunt = UserProfile('Ivan@gmail.cry', '234', 'Obicniy')
# print(accaunt.login('Ivan@gmail.cry', '123'))
