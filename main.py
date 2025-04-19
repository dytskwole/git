import numpy as np 


class Car:
    def __init__(self, speed):
        self.speed = speed
        self.check_speed()
        
    def check_speed(self):
        if self.speed >= 100:
            print("Шумахер ты")
        else: 
            print("добавь газку!")

car = Car(110)


arr = np.array(
    [[1,23,4],
    [4,6,7],
    [43,68,1]]
)
print(arr.shape)


print("hello pyhon")

try:
    print('Попробуем что-нибудь написать')
except Exception as e:
    print(f'Произошла ошибка: {e}')

for i in range(4):
    for j in range(4):
        print("*", end="")
    print()