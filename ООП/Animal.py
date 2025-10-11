class Animal:
    def __init__(self, kg, color, title, eat):
        self.kg = kg
        self.color = color
        self.title = title
        self.eat = eat

    def __str__(self):
        return f'Вид: {self.title}\nОкрас: {self.color}\nЕст: {self.eat}\nВесит: {self.kg}кг'

class Hydrobiont(Animal):
    def __init__(self, kg, color, title, eat, swim_speed):
        super().__init__(kg, color, title, eat)
        self.swim_speed = swim_speed

    def __str__(self):
        return super().__str__()+f'\nСкорость плаванья: {self.swim_speed}км/ч'

class Terrestrial(Animal):
    def __init__(self, kg, color, title, eat, run_speed):
        super().__init__(kg, color, title, eat)
        self.run_speed = run_speed

    def __str__(self):
        return super().__str__()+f'\nМакс скорость бега: {self.run_speed}км/ч'

cat = Terrestrial(kg=5,color='Черный',title="Бомбейская кошка",eat='Мясо',run_speed=30)
print(cat)

shark = Hydrobiont(title='Акула молот',color='Серо-белая',eat='Рыбу',kg=50,swim_speed=40)
print(shark)