import random

eror_1 = "‼️Вы ввели что-то не то‼️"
eror_2 = "‼️Ошибка‼️ 001"
end_1 = "🚨❗Вы проиграли❗🚨"

user_name = str(input("Введите ваше прозвище: "))

print("Прошу вводить всё с маленькой буквы")
while True:
    try:
        edu = str(input("Хотите посмотреть на управление? да или нет?\n"))
        if edu == "да":
            print('"ц" перестроится вверх\n"ы" перестроится вниз\n"ф" продолжить движение вперёд')
            break
        elif edu == "нет":
            print("Как хотите")
            break
        else:
            print(eror_1)
    except ValueError:
        print(eror_2)

up = "ц"
down = "ы"
forward = "ф"

while True:
    try:
        control = str(input("Хотите поменять управление? да или нет?\n"))
        if control == "да":
            up = str(input("Введите символ для перестроеня в верх: "))
            down = str(input("Введите символ для перестроеня вниз: "))
            forward = str(input("Введите символ для продолжения движения: "))
            break
        elif control == 'нет':
            break
        else:
            print(eror_1)
    except ValueError:
        print (eror_2)
        

while True:
    try:
        start = str(input("Хотите начать? да или нет?\n"))
        if start == "да":
            print("Загрузка...")
            break
        elif start == "нет":
            raise SystemExit("Прка :(")
        else:
            print("‼️Вы ввели что-то не то‼️")
    except ValueError:
        print(eror_2)

border = "➖➖➖➖➖➖➖"
line = "--------------"

cars = ["🚗","🚛","🚐","🏎️","🦽","🚕","🚙","🚒","🚑","🚓","🚚","🚜","🚌","🏍️","🚴"]

while True:
    try:
        userCar = int(input("НАПИШИТЕ НОМЕР ВЫБРАННОЙ МАШИНЫ\nВыберите машину:\n1.🚗\n2.🚛\n3.🚐\n4.🏎️\n5.🦽\n"))
        if userCar == 1:
            userCar = cars[0]
            break
        elif userCar == 2:
            userCar = cars[1]
            break
        elif userCar == 3:
            userCar = cars[2]
            break
        elif userCar == 4:
            userCar = cars[3]
            break
        elif userCar == 5:
            userCar = cars[4]
            break
        else:
            print("‼️ВВЕДИТЕ НОМЕР ВЫБРАННОЙ МАШИНЫ‼️")
    except ValueError:
        print(eror_2)

car_0 = cars[5]

print("Вы едите c право налево⬅️")

exp = 0

while True:
    try:
        car_1 = random.choice(cars)
        car_2 = random.choice(cars)
        car_3 = random.choice(cars)

        frames = [f"{border}\n{car_1}          {userCar}\n{line}\n            {car_0}\n{border}\n",
          f"{border}\n\n{line}\n        {car_0}💥{userCar}\n{border}",
          f"{border}\n   {car_1}       {userCar}\n{line}\n\n{border}",
          f"{border}\n   {car_1}\n{line}\n            {userCar}\n{border}",
          f"{border}\n      {car_1}    {userCar}\n{line}\n\n{border}",
          f"{border}\n      {car_1}\n{line}\n            {userCar}\n{border}",
          f"{border}\n         {car_1} {userCar}\n{line}\n{car_2}\n{border}",
          f"{border}\n         {car_1}\n{line}\n{car_2}          {userCar}\n{border}",
          f"{border}\n        {car_1}💥{userCar}\n{line}\n   {car_2}\n{border}",
          f"{border}\n            {car_1}\n{line}\n   {car_2}       {userCar}\n{border}",
          f"{border}\n            {userCar}\n{line}\n      {car_2}\n{border}",
          f"{border}\n\n{line}\n      {car_2}    {userCar}\n{border}",
          f"{border}\n{car_3}          {userCar}\n{line}\n         {car_2}\n{border}",
          f"{border}\n{car_3}\n{line}\n         {car_2} {userCar}\n{border}",
          f"{border}\n   {car_3}       {userCar}\n{line}\n            {car_2}\n{border}",
          f"{border}\n   {car_3}\n{line}\n        {car_2}💥{userCar}\n{border}",
          f"{border}\n      {car_3}    {userCar}\n{line}\n{car_0}\n{border}",
          f"{border}\n      {car_3}\n{line}\n{car_0}          {userCar}\n{border}",
          f"{border}\n         {car_3} {userCar}\n{line}\n   {car_0}\n{border}",
          f"{border}\n         {car_3}\n{line}\n   {car_0}       {userCar}\n{border}",
          f"{border}\n        {car_3}💥{userCar}\n{line}\n      {car_0}\n{border}",
          f"{border}\n            {car_3}\n{line}\n      {car_0}    {userCar}\n{border}",
          f"{border}\n            {userCar}\n{line}\n         {car_0}\n{border}",
          f"{border}\n\n{line}\n         {car_0} {userCar}\n{border}",]

        step = str(input(frames[0]))

        if exp >= 3:
            raise SystemExit(f"Поздравляю {user_name} с победой")
        else:
            print()
        while True:
            try:
                if step in [forward, up]:
                    print(frames[2])
                    userPosition = "1"
                    break
                elif step == down:
                    print(frames[3])
                    userPosition = "2"
                    break
                else:
                    print(eror_1)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward,up]:
                        print(frames[4])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[5])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[4])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[5])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[6])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[7])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[6])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[7])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[8])
                        raise SystemExit(end_1)
                    elif step == down:
                        print(frames[9])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[8])
                        raise SystemExit(end_1)
                    elif step in [forward, down]:
                        print(frames[9])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "2":
                    if step == up:
                        print(frames[10])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[11])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[12])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[13])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[12])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[13])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[14])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[15])
                        raise SystemExit(end_1)
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[14])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[15])
                        raise SystemExit(end_1)
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[16])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[17])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[16])
                        userPosition = "1"
                        break
                    elif step [forward, down]:
                        print(frames[17])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[18])
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[19])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[18])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[19])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        print(frames[20])
                        raise SystemExit(end_1)
                    elif step == down:
                        print(frames[21])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        print(frames[20])
                        raise SystemExit(end_1)
                    elif step in [forward, down]:
                        print(frames[21])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "2":
                    if step == up:
                        print(frames[22])
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[23])
                        userPosition = "2"
                        break
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)

        while True:
            try:
                step = str(input())
                if userPosition == "1":
                    if step in [forward, up]:
                        userPosition = "1"
                        break
                    elif step == down:
                        print(frames[1])
                        raise SystemExit(end_1)
                    else:
                        print(eror_1)
                elif userPosition == "2":
                    if step == up:
                        userPosition = "1"
                        break
                    elif step in [forward, down]:
                        print(frames[1])
                        raise SystemExit(end_1)
                    else:
                        print(eror_1)
                else:
                    print(eror_2)
            except ValueError:
                print(eror_2)
        exp = exp + 1
    except ValueError:
        print(eror_2)