class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Car:  # An unrelated class that also implements make_sound()
    def make_sound(self):
        return "Vroom vroom!"

def process_sound(sound_object):
    """Process any object that implements make_sound()"""
    print(f"Sound produced: {sound_object.make_sound()}")

# Demonstration
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    car = Car()

    # The same function works with different types
    process_sound(dog)  # Output: Sound produced: Woof!
    process_sound(cat)  # Output: Sound produced: Meow!
    process_sound(car)  # Output: Sound produced: Vroom vroom!