import random, matplotlib.pyplot as plt

class Particle:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.x_positions = [x]
        self.y_positions = [y]
        self.t = 0
        
    def move(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.x += 1
        elif direction == 2:
            self.y += 1
        elif direction == 3:
            self.x -= 1
        elif direction == 4:
            self.y -= 1
        self.x_positions.append(self.x)
        self.y_positions.append(self.y)
        self.t += 1
    
class Particles:
    def __init__(self, particles):
        self.particles = particles
        
    def move(self):
        for particle in self.particles:
            particle.move()
    
    def plot(self):
        x_values = [particle.x for particle in self.particles]
        y_values = [particle.y for particle in self.particles]
        plt.plot(x_values, y_values, 'bo')
        plt.show()
        
    def moves(self, n):
        for i in range(n):
            self.move()
            
if __name__ == '__main__':
    particles = Particles([Particle(0, 0) for i in range(25)])
    particles.moves(50)
    particles.plot()
