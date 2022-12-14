import pygame

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.width = 448
        self.height = 720
        self.caption = "Bubble_Bubble"
        self.screen = self.set_screen()
        self.running = True
    
    def set_screen(self):
        pygame.display.set_caption (self.caption)
        return pygame.display.set_mode((self.width, self.height))

    def set_game_environment(self):
        while self.running:

            self.set_frame_rate()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
        
    def set_frame_rate(self):
        frame_rate = 60
        self.clock.tick(frame_rate)

    
def main():
    pygame.init()

    game = Game()
    game.set_game_environment()
            
    pygame.quit()


    
if __name__ == "__main__":
    main()