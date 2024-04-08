from S1E9 import Character


class Baratheon(Character):
    """Your docstring for Class Baratheon"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    def die(self):
        """Your docstring for Method die"""
        super().die()


class Lannister(Character):
    """Your docstring for Class Lannister"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    def die(self):
        """Your docstring for Method die"""
        super().die()
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for Method create lannister"""
        return cls(first_name, is_alive)