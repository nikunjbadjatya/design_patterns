# Take a look at this approach as well
# http://elbenshira.com/blog/singleton-pattern-in-python/


class Singleton(object):
	__firstinstance = None

	def __init__(self):
		print("In init")

	def __new__(cls):
		print("In new")
		if not cls.__firstinstance:
			print("Creating first instance")
			cls.__firstinstance = super(Singleton, cls).__new__(cls)
		return cls.__firstinstance

i = Singleton()
print(id(i))
j = Singleton()
print(id(j))

