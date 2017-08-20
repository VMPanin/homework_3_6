class Animal:
    can_fly = None # bool
    sound = None # string
    name = None # string

    def __init__(self, **kwargs):
        self.name = kwargs['name']

    def say_sound(self):
        print(self.sound)

    def fly(self):
        if self.can_fly:
            print("My name is {}. I'm flying!!!".format(self.name))
        if not self.can_fly:
            print("My name is {}. Sorry, I can not fly".format(self.name))


class Cattle(Animal):
    can_fly = False


class Bird(Animal):
    can_fly = True


class Cow(Cattle, Animal):
    sound = "mooooo"


class Goat(Cattle, Animal):
    sound = "beeeee"


class Sheep(Cattle, Animal):
    sound = "meeeeee"


class Pig(Cattle, Animal):
    sound = "khruu"


class Duck(Bird, Animal):
    sound = "krya-krya"


class Chicken(Bird, Animal):
    sound = "kokoko"


class Goose(Bird, Animal):
    sound = "goooooose"

pig_1 = Pig(name="Zelda")
print(pig_1.name)
pig_1.say_sound()

duck_1 = Duck(name="Donald")
duck_1.fly()
