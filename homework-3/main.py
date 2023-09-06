from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    print(moscowpython)
    print(highload)
    print("Количество подписчиков на канале MoscowPython:", moscowpython.subscribers)
    print("Количество подписчиков на канале HighLoad Channel:", highload.subscribers)

    sum_total = moscowpython + highload
    difference = highload - moscowpython

    print("Сумма подписчиков двух объектов:", sum_total)
    print("Разница подписчиков двух объектов:", difference)
    print("moscowpython > highload:", moscowpython > highload)
    print("moscowpython >= highload:", moscowpython >= highload)
    print("moscowpython < highload:", moscowpython < highload)
    print("moscowpython <= highload:", moscowpython <= highload)
    print("moscowpython == highload:", moscowpython == highload)



    
