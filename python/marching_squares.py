import pygame
import random
import math


'''
Constants
'''
WIDTH = 800
HEIGHT = 600
FPS = 100

grid = 1

'''
Distance between two points
'''
def dist(p1, p2):
    return math.ceil((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)



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


def marching_squares(hm , screen):
    for i in range(0 , WIDTH , grid):
        for j in range(0 ,HEIGHT , grid):
            case = "".join(map(str , [hm[i,j] , hm[i+grid,j] , hm[i+grid,j+grid] , hm[i,j+grid]]))
            if case == "0000":
                pass
            elif case == "0001":
                pygame.draw.line(screen, (0, 0, 0), (i, j + grid // 2), (i+grid // 2, j + grid))
            elif case == "0010":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j + grid), (i + grid, j + grid // 2))
            elif case == "0011":
                pygame.draw.line(screen, (0, 0, 0), (i , j + grid // 2), (i + grid , j + grid // 2))
            elif case == "0100":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j), (i + grid , j + grid // 2))
            elif case == "0101":
                pygame.draw.line(screen, (0, 0, 0), (i , j + grid // 2), (i + grid // 2, j ))
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j + grid), (i + grid , j + grid // 2))
            elif case == "0110":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j), (i + grid // 2, j + grid))
            elif case == "0111":
                pygame.draw.line(screen, (0, 0, 0), (i , j + grid // 2), (i + grid // 2, j ))
            elif case == "1000":
                pygame.draw.line(screen, (0, 0, 0), (i , j + grid // 2), (i + grid // 2, j ))
            elif case == "1001":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j), (i + grid // 2, j + grid))
            elif case == "1010":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j), (i + grid , j + grid // 2))
                pygame.draw.line(screen, (0, 0, 0), (i, j + grid // 2), (i + grid//2 , j + grid))
            elif case == "1011":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j), (i + grid , j + grid // 2))
            elif case == "1100":
                pygame.draw.line(screen, (0, 0, 0), (i , j + grid // 2), (i + grid , j + grid // 2))
            elif case == "1101":
                pygame.draw.line(screen, (0, 0, 0), (i + grid // 2, j + grid), (i + grid , j + grid // 2))
            elif case == "1110":
                pygame.draw.line(screen, (0, 0, 0), (i, j + grid // 2), (i + grid//2 , j + grid))
            elif case == "1111":
                pass




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
            
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        

    def update(self):
        for ball in self.balls:
            ball.update()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def draw(self ):
        self.screen.fill((255, 255, 255))
        hm = {}
        for i in range(0, WIDTH + grid, grid):
            for j in range(0 , HEIGHT + grid, grid):
                color = 0
                for ball in self.balls:
                    distance = dist((i, j), (ball.x, ball.y))
                    if distance:
                        color += (ball.radius**2) / distance
                    else:
                        color = 0.5
                if color >  0.2:
                    hm[i,j] = 1
                else:
                    hm[i,j] = 0
        marching_squares(hm , self.screen)


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