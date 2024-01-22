import pygame
import random
import math
import threading


'''
Constants
'''
WIDTH = 1200
HEIGHT = 800
FPS = 1
THREADS = 100
CELL = 1

'''
Distance between two points
'''
def dist(p1, p2):
    return math.ceil(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))



'''
Ball Class
'''
class Ball:
    def __init__(self):
        self.radius = random.randint(20, 50)
        self.x = random.randint(0, WIDTH - self.radius)
        self.y = random.randint(0, HEIGHT - self.radius)
        self.speedx = random.randint(-30, 30)
        self.speedy = random.randint(-30, 30)
        
    
    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x < 0 or self.x > WIDTH - self.radius:
            self.speedx *= -1
        if self.y < 0 or self.y > HEIGHT - self.radius:
            self.speedy *= -1



'''
Main class
'''
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.balls = [Ball() , Ball() , Ball() , Ball() , Ball() , Ball()]

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.screen.fill((255, 255, 255))
            ts = []
            for i in range(THREADS):
                # self.draw(i)
                t = threading.Thread(target=self.draw, args=(i,))
                t.start()
                ts.append(t)
            for t in ts:
                t.join()
            pygame.display.flip()
            # self.clock.tick(FPS)
        

    def update(self):
        for ball in self.balls:
            ball.update()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def draw(self , thread):
        
        for i in range((WIDTH // THREADS) * thread  , (WIDTH // THREADS) * (thread + 1) , CELL):
            for j in range(0 , HEIGHT , CELL):
                color = 0
                for ball in self.balls:
                    color += (ball.radius**2)*6//(dist((i, j), (ball.x, ball.y)) + 1)
                if color>255:
                    pygame.draw.circle(self.screen, (0, 0, 0), (i, j), CELL//4)

        



'''
main function
'''

def main():
    main = Main()
    main.run()



'''
calling main function
'''
if __name__ == '__main__':
    main()