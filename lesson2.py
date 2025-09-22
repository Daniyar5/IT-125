flags = {
    'ru': {'red blue', 'white'},
    'kg': {"red yellow", 'red'},
    'ua': {"red blue", 'red', 'blue'},
    'uk': {"yellow", "blue"},
    'kz': {'blue yellow', 'blue'},
    'jp': {"white red", "white", "red"},
    'Gm': {'black red yellow', 'black', 'red' , 'yellow'},
    'USSR': {'red yellow', 'red', 'yellow'}
}
    
while True:
    color = str(input('Введите цвет: '))
    if color == "exit":
            break
    for key, value in flags.items():
        if color in value:
            print(key)