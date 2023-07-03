from abc import ABC, abstractmethod

class Building(ABC):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @abstractmethod
    def construct(self):
        pass

    @abstractmethod
    def demolish(self):
        pass
