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