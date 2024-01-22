import pygame
import random
import math


'''
Constants
'''
WIDTH = 1024 
HEIGHT = 512
FPS = 100

LOWEST_GRID = 2


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
        self.speedx = random.randint(-20, 20)
        self.speedy = random.randint(-20, 20)
        
    
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
        self.screen = pygame.display.set_mode((WIDTH + 1 , HEIGHT + 1))
        self.clock = pygame.time.Clock()
        self.running = False
        self.balls = [Ball() , Ball() , Ball() , Ball() , Ball() , Ball()]

    def run(self):
        while self.running:
            self.events()
            self.update()
            
            self.draw()
            pygame.display.flip()
            # self.clock.tick(FPS)
        

    def update(self):
        for ball in self.balls:
            ball.update()
            

    def events(self):
        global LOWEST_GRID
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    LOWEST_GRID = min(LOWEST_GRID*2 , 16)
                if event.key == pygame.K_a:
                    LOWEST_GRID = max(LOWEST_GRID//2, 1)

                if event.key == pygame.K_RETURN:
                    self.running = True
                    self.run()



    def calculate_value(self, i, j):
        if (i,j) in self.hm:
            return

        value = 0
        for ball in self.balls:
            distance = dist((i, j), (ball.x, ball.y))
            if distance:
                value += (ball.radius**2) / distance
            else:
                value = 0.5
        if value >  0.2:
            self.hm[i,j] = 1
        else:
            self.hm[i,j] = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.hm = {}
        self.marching_squares(start_width = 0 ,end_width = WIDTH, start_height = 0, end_height = HEIGHT , grid = 16)
        font = pygame.font.SysFont("arial", 30)
        text = font.render("Smallest Cell : " + str(LOWEST_GRID), True, (0, 0, 0))
        self.screen.blit(text, (WIDTH - text.get_width() - 10, HEIGHT - text.get_height() - 10))
    
    
    def marching_squares(self, start_width, end_width, start_height, end_height, grid):
        for i in range(start_width, end_width + 1 , grid):
            for j in range(start_height, end_height + 1 , grid):
                self.calculate_value(i, j)
                self.calculate_value(i + grid, j)
                self.calculate_value(i + grid, j + grid)
                self.calculate_value(i, j + grid)
                case = "".join(map(str , [self.hm[i,j] , self.hm[i + grid, j] , self.hm[i + grid, j + grid] , self.hm[i, j + grid]]))
                if case != "0000" and case != "1111" and grid > LOWEST_GRID:
                    self.marching_squares(i, i + grid, j, j + grid, grid // 2)
                elif case != "0000" and case != "1111" and grid == LOWEST_GRID:
                    if case == "0001":
                        pygame.draw.line(self.screen, (33,33,33), (i, j + grid // 2), (i+grid // 2, j + grid) )
                    elif case == "0010":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j + grid), (i + grid, j + grid // 2))
                    elif case == "0011":
                        pygame.draw.line(self.screen, (33,33,33), (i , j + grid // 2), (i + grid , j + grid // 2))
                    elif case == "0100":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j), (i + grid , j + grid // 2))
                    elif case == "0101":
                        pygame.draw.line(self.screen, (33,33,33), (i , j + grid // 2), (i + grid // 2, j ))
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j + grid), (i + grid , j + grid // 2))
                    elif case == "0110":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j), (i + grid // 2, j + grid))
                    elif case == "0111":
                        pygame.draw.line(self.screen, (33,33,33), (i , j + grid // 2), (i + grid // 2, j ))
                    elif case == "1000":
                        pygame.draw.line(self.screen, (33,33,33), (i , j + grid // 2), (i + grid // 2, j ))
                    elif case == "1001":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j), (i + grid // 2, j + grid))
                    elif case == "1010":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j), (i + grid , j + grid // 2))
                        pygame.draw.line(self.screen, (33,33,33), (i, j + grid // 2), (i + grid//2 , j + grid))
                    elif case == "1011":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j), (i + grid , j + grid // 2))
                    elif case == "1100":
                        pygame.draw.line(self.screen, (33,33,33), (i , j + grid // 2), (i + grid , j + grid // 2))
                    elif case == "1101":
                        pygame.draw.line(self.screen, (33,33,33), (i + grid // 2, j + grid), (i + grid , j + grid // 2))
                    elif case == "1110":
                        pygame.draw.line(self.screen, (33,33,33), (i, j + grid // 2), (i + grid//2 , j + grid))




    def home_screen(self):
        '''
        Draw a simple home screen with text showing the intructions to speed up and down
        '''
        while not self.running:
            self.screen.fill((255, 255, 255))
            font = pygame.font.SysFont('Arial', 30)
            text = font.render("Press 'd' and 'a' to increase and decrease no of grid size", True, (0, 0, 0))
            text2 = font.render("Press ENTER TO START", True, (0, 0, 0))

            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            self.screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 - text2.get_height() // 2 + 50))
            pygame.display.flip()
            self.events()
            


'''
main function
'''

def main():
    main = Main()
    main.home_screen()



'''
calling main function
'''
if __name__ == '__main__':
    main()