### creating a working physics engine in python ###

import pygame
import numpy as np

# main
def main():
    load_screen()
    

class PhysicsBody:
    def __init__(self, shape="circle", speed=200, jump_v=500):
        self.shape: str = shape # change this eventually to be based on user input
        self.SPEED: int = speed
        self.JUMP_V: int = jump_v

        #constants
        self.pos = pygame.Vector2(600,300)
        self.GRAVITY: int = 980
        self.y_velocity: int = 0
        
    
    def update(self, dt):
        self.move(dt)
        self.gravity(dt)

    def move(self, dt):
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.pos.x -= self.SPEED * dt
        if keys[pygame.K_d]:
            self.pos.x += self.SPEED * dt
        if keys[pygame.K_SPACE]:
            self.pos.y -= self.JUMP_V * dt
        
    def gravity(self, dt):
        if self.pos.y >= 600:
            self.pos.y = 600
            self.y_velocity = 0
        else: 
            self.y_velocity += self.GRAVITY * dt 
            self.pos.y += self.y_velocity * dt

    def collision(self, dt, enabled=True):
        if self.pos.y == self.pos.y:
            pass
        
            
    def draw(self, screen):
         pygame.draw.circle(screen, "red", self.pos, 40)

class FixedObject: 
    def __init__(self, x=300, y=300, shape='rect'):
        self.shape: str = shape
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
         rect = pygame.Rect(100, 200, 40, 40)
         pygame.draw.rect(screen, "red", rect)



# graphical interface 
def load_screen(): 

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    player = PhysicsBody("circle", 300)
    player2 = PhysicsBody(speed=400, jump_v=400)
    obstacle = FixedObject()
   
    running = True

    while running:
        # Framerate = 60 FPS
        dt = clock.tick(60) / 1000

        #Handle Quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Erase display
        screen.fill("black")

        # Main Processes 
        player2.update(dt)
        player.update(dt)

        # New display
        player.draw(screen)
        player2.draw(screen)
        obstacle.draw(screen)

        pygame.display.update() 

    pygame.quit()




def run_engine():
    pass 

def normalize(x , y): 
    length = np.sqrt(x**2 + y**2)
    return((x / length), (y / length))


# kinematics 



# gravity 


# trajectories / ballistics 

# collisions
def handle_collisions():
    pass
   # if PhysicsBody.position = PhysicsBody.position:
    


# centripetal motion

# springs and potential energy

# tests and evaulations 

# datasets 

# extra: light, ray tracing 

if __name__ == "__main__":
    main()
