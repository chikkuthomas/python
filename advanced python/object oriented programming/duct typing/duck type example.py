class Swift:
    def start(self):
        print("start swift car")
    def accelerate(self):
        print("swift car accelerating")
    def stop(self):
        print("swift car is stopping")
class Audi:
    def start(self):
        print("audi is starting")
    def accelerate(self):
        print("audi car is accelerating")
    def stop(self):
        print("audi car is stopping")
class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()
p=Person()
sw=Swift()
p.drive(sw)
print()
ad=Audi()
p.drive(ad)
