class Zoo_show():
    def __init__(self, guest):
        self.guest = guest

    def __str__(self):
        return f'{self.guest}'
    
class Ticket():
    def __init__(self, ticket):
        self.ticket = ticket

    def __str__(self):
        return f'Отличный выбор: \n{self.ticket}'
        
ticket_1 = Ticket(ticket='Ты идёш смотреть как жанглирует горила')
ticket_2 = Ticket(ticket='Ты идёш смотреть как медведь катается на одноколёстом велосипеде по тонкому канату')

guest_1 = Zoo_show(guest=f'Дорогой гость, добро пожаловать в Шоу Зверей!\
                            \nУ нас имеются такие шоу как:\
                            \n1.Жанглирование горилой шарами для боулинга\
                            \n2.Катание медведя на одноколосном велосипеде по тонкому канату\
                            \nВыберите номер билета: ')
choice = input(guest_1)

if choice == '1':
    print(ticket_1)
elif choice == '2':
    print(ticket_2)
else:
    print('Такого билета нет')