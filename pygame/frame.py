import os
import pygame
CURRENT_PATH = os.path.dirname(__file__)

class Screen:
    def __init__(self) -> None:
        self.width = 448
        self.height = 720
        self.caption = "Bubble_Bubble"
        self.background = pygame.image.load(os.path.join(CURRENT_PATH, "background.png"))

    def set_screen(self):
        pygame.display.set_caption (self.caption)
        return pygame.display.set_mode((self.width, self.height)).blit(self.background, (0, 0))


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = Screen().set_screen()

    def set_game_loop(self):
        while self.running:

            self.set_frame_rate()

            self.manage_events()
            
            pygame.display.update()
        
    def set_frame_rate(self):
        frame_rate = 60
        self.clock.tick(frame_rate)

    def manage_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    
def main():
    pygame.init()

    game = Game()
    game.set_game_loop()
            
    pygame.quit()


    
if __name__ == "__main__":
    main()