import time
import random

class Sonic:
    def __init__(self):
        self.rings = 0
        self.alive = True

    def collect_ring(self):
        self.rings += 1
        print("Sonic collected a ring! Total rings:", self.rings)

    def hit_obstacle(self):
        if self.rings > 0:
            self.rings -= 1
            print("Sonic hit an obstacle! Lost a ring. Total rings:", self.rings)
        else:
            self.alive = False
            print("Sonic hit an obstacle and has no rings left! Game Over.")

    def run(self):
        while self.alive:
            action = random.choice(['run', 'collect_ring', 'hit_obstacle'])
            if action == 'collect_ring':
                self.collect_ring()
            elif action == 'hit_obstacle':
                self.hit_obstacle()
            time.sleep(1)

if __name__ == "__main__":
    sonic = Sonic()
    try:
        sonic.run()
    except KeyboardInterrupt:
        print("Game interrupted. Final ring count:", sonic.rings)