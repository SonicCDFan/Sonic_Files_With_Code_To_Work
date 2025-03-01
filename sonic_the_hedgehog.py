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