#from dog import Dog
# The Client-2's Dog;s implementation does not have any 'say' method. Rather they have 'bark' method.
# We want to make use of their Dog implementation at the same time it should work in our legact system 
# with as less changes as possible.
# DogAdapter class does this for us.

class Dog(object):
    """This is actually coming from some 3rd party"""
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "bark"

class Person(object):
    """ Client-1 has this definition of 'say' for a Person"""
    def __init__(self, name):
        self.name = name

    def say(self):
        return "hello"

class DogAdapter(object):
    """Adapts the Dog class through encapsulation"""

    def __init__(self, canine):
        # This adapters instance will hold the instance of actual dog class
        self.canine = canine

    def say(self):
        """The adapted method"""
        return self.canine.bark()

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)

def main():
    p1 = Person('Bob')
    da1 = DogAdapter(Dog('Newton'))

    creatures = [p1, da1]
    for creature in creatures:
        print (creature.name, creature.say())

if __name__ == '__main__':
    main()