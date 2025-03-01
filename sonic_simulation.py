import time
import random

class Sonic:
    def __init__(self, name="Sonic"):
        self.name = name
        self.rings = 0
        self.distance = 0

    def run(self):
        print(f"{self.name} is running...")
        for _ in range(10):
            self.distance += random.randint(1, 10)
            self.collect_rings()
            self.display_status()
            time.sleep(1)
        print(f"{self.name} finished running!")

    def collect_rings(self):
        rings_found = random.randint(0, 5)
        self.rings += rings_found
        if rings_found > 0:
            print(f"{self.name} found {rings_found} rings!")

    def display_status(self):
        print(f"{self.name} has {self.rings} rings and has run {self.distance} meters.")

if __name__ == "__main__":
    sonic = Sonic()
    sonic.run()