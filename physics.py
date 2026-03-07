### creating a working physics engine in python ###

import pygame
import numpy as np

# main
def main():
    load_screen()
    

class PhysicsBody:
    def __init__(self, shape):
        self.shape = shape # change this eventually to be based on user input

        #constants
        self.pos = pygame.Vector2(600,300)
        self.GRAVITY = 980
        self.y_velocity = 0
    
    def update(self, dt):
        self.move()
        self.gravity()

    def move(self, dt):
    
        self.SPEED: int = 300
        self.JUMP_V: int = 600
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
            
    def draw(self, screen):
         pygame.draw.circle(screen, "red", self.pos, 40)



# graphical interface 
def load_screen(): 

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    player = PhysicsBody("circle")
    player2 = PhysicsBody("circle")
   
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
        
        player.update(dt)

        # New display
        player.draw(screen)

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
