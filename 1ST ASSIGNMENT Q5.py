from abc import ABC, abstractmethod

class SoundMaker(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

class Dog(SoundMaker):
    def make_sound(self):
        return "Woof!"

# Now `Dog` must implement `.make_sound()`, or Python raises an error.
class Duck:
    def make_sound(self):
        return "Quack!"

duck = Duck()


def process_sound(duck):
    pass
from typing import Protocol

class SoundProtocol(Protocol):
    def make_sound(self) -> str: ...

def process_sound(sound_object: SoundProtocol) -> None:
    print(f"Sound produced: {sound_object.make_sound()}")


process_sound(duck)  # Output: Sound produced: Quack!