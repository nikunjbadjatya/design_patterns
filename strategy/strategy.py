
class Fly(object):
	def fly(self):
		raise NotImplementedError

class CantFly(Fly):
	def fly(self):
		print("Cant fly")

class ItFlys(Fly):
	def fly(self):
		print("Flying high")

class Animal(object):
    def set_flying_ability(self, fly_type):
        self.flying_type = fly_type

    def try_to_fly(self):
    	self.flying_type.fly()

class Dog(Animal):
	def __init__(self):
		self.flying_type = CantFly()

class Bird(Animal):
	def __init__(self):
		self.flying_type = ItFlys()


def main():
	dog = Dog()
	bird = Bird()

	dog.try_to_fly()
	bird.try_to_fly()

	dog.set_flying_ability(ItFlys())

	dog.try_to_fly()

if __name__ == '__main__':
	main()