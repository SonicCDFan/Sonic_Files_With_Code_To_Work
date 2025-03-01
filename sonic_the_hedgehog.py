class Sonic:
    def __init__(self, name="Sonic", speed=100):
        self.name = name
        self.speed = speed

    def run(self):
        return f"{self.name} is running at {self.speed} mph!"

    def spin_dash(self):
        return f"{self.name} is performing a Spin Dash!"

class Tails(Sonic):
    def __init__(self, name="Tails", speed=80, fly_speed=60):
        super().__init__(name, speed)
        self.fly_speed = fly_speed

    def fly(self):
        return f"{self.name} is flying at {self.fly_speed} mph!"

class Knuckles(Sonic):
    def __init__(self, name="Knuckles", speed=70, strength=100):
        super().__init__(name, speed)
        self.strength = strength

    def punch(self):
        return f"{self.name} is punching with a strength of {self.strength}!"

# Example usage
sonic = Sonic()
tails = Tails()
knuckles = Knuckles()

print(sonic.run())
print(sonic.spin_dash())
print(tails.run())
print(tails.fly())
print(knuckles.run())
print(knuckles.punch())

class Sonic:
    def __init__(self, name: str = "Sonic", speed: int = 100):
        """
        Initialize a Sonic character.

        Args:
            name (str): The name of the character.
            speed (int): The running speed of the character.
        """
        self.name = name
        self.speed = speed

    def run(self) -> str:
        """
        Return a string describing the character running.

        Returns:
            str: A description of the character running at their speed.
        """
        return f"{self.name} is running at {self.speed} mph!"

    def spin_dash(self) -> str:
        """
        Return a string describing the character performing a spin dash.

        Returns:
            str: A description of the character performing a spin dash.
        """
        return f"{self.name} is performing a Spin Dash!"

class Tails(Sonic):
    def __init__(self, name: str = "Tails", speed: int = 80, fly_speed: int = 60):
        """
        Initialize a Tails character.

        Args:
            name (str): The name of the character.
            speed (int): The running speed of the character.
            fly_speed (int): The flying speed of the character.
        """
        super().__init__(name, speed)
        self.fly_speed = fly_speed

    def fly(self) -> str:
        """
        Return a string describing the character flying.

        Returns:
            str: A description of the character flying at their speed.
        """
        return f"{self.name} is flying at {self.fly_speed} mph!"

class Knuckles(Sonic):
    def __init__(self, name: str = "Knuckles", speed: int = 70, strength: int = 100):
        """
        Initialize a Knuckles character.

        Args:
            name (str): The name of the character.
            speed (int): The running speed of the character.
            strength (int): The strength of the character.
        """
        super().__init__(name, speed)
        self.strength = strength

    def punch(self) -> str:
        """
        Return a string describing the character punching.

        Returns:
            str: A description of the character punching with their strength.
        """
        return f"{self.name} is punching with a strength of {self.strength}!"

# Example usage
sonic = Sonic()
tails = Tails()
knuckles = Knuckles()

print(sonic.run())
print(sonic.spin_dash())
print(tails.run())
print(tails.fly())
print(knuckles.run())
print(knuckles.punch())
