from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
    @abstractmethod
    def die(self):
        """Your docstring for Method die"""
        self.is_alive = False
    def __str__(self):
        """Your docstring for Method __str__"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"
    def __repr__(self):
        """Your docstring for Method __repr__"""
        return self.__str__()

class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False