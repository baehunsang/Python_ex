import os
import pygame

CURRENT_PATH = os.path.dirname(__file__)
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
SCREEN_WIDTH = 448
SCREEN_HEIGHT = 720
ANGLE_SPEED = 1.5
MAX_RIGHT_ANGLE = 10
MAX_LEFT_ANGLE = 170
POINTER_POSITION = (SCREEN_WIDTH // 2, 624)

class Image:
    def __init__(self):
        self.background = self.load_background_image()
        self.bubble_images = [
            pygame.image.load(os.path.join(CURRENT_PATH, "red.png")).convert_alpha(),
            pygame.image.load(os.path.join(CURRENT_PATH, "yellow.png")).convert_alpha(),
            pygame.image.load(os.path.join(CURRENT_PATH, "blue.png")).convert_alpha(),
            pygame.image.load(os.path.join(CURRENT_PATH, "green.png")).convert_alpha(),
            pygame.image.load(os.path.join(CURRENT_PATH, "purple.png")).convert_alpha(),
            pygame.image.load(os.path.join(CURRENT_PATH, "black.png")).convert_alpha()
        ]
        self.pointer_image = pygame.image.load(os.path.join(CURRENT_PATH, "pointer.png"))

    def load_background_image(self):
        return pygame.image.load(os.path.join(CURRENT_PATH, "background.png"))

    def get_background(self):
        return self.background

    def get_bubbles(self):
        return self.bubble_images

    def get_pointer(self):
        return self.pointer_image

class Screen:
    def __init__(self) -> None:
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.caption = "Bubble_Bubble"

    def set_screen(self):
        pygame.display.set_caption (self.caption)
        return pygame.display.set_mode((self.width, self.height))

class Pointer(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = image.get_rect(center=POINTER_POSITION)
        self.angle = 90

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self, total_angle):
        self.angle += total_angle
        if self.angle <= MAX_RIGHT_ANGLE:
            self.angle = MAX_RIGHT_ANGLE 

        elif self.angle >= MAX_LEFT_ANGLE:
            self.angle = MAX_LEFT_ANGLE 

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=POINTER_POSITION)


class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)
        
class Map:
    def __init__(self, bubble_images) -> None:
        self.map = []
        self.bubble_group = Bubble_Group(bubble_images)

    def setup(self):
        self.map = [
            # '/' 는 bubble이 들어갈 수 없는 곳
            # '.' 은 빈칸
            list("RRYYBBGG"),
            list("RRYYBBG/"),
            list("BBGGRRYY"),
            list("BGGRRYY/"),
            list("........"),
            list("......./"),
            list("........"),
            list("......./"),
            list("........"),
            list("......./"),
            list("........")
        ]

    def get_map(self):
        return self.map


class Bubble_Group:
    def __init__(self, bubble_images) -> None:
        self.bubble_images = bubble_images
        self.bubble_group = pygame.sprite.Group()
    
    def get_bubble_position(self, row_idx, col_idx):
        x_position = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
        y_position = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)

        if row_idx % 2 == 1:
            x_position += CELL_SIZE // 2
        
        return (x_position, y_position)

    def get_bubble_image(self, sell):
        if sell == "R":
            return self.bubble_images[0]

        elif sell == "Y":
            return self.bubble_images[1]

        elif sell == "B":
            return self.bubble_images[2]

        elif sell == "G":
            return self.bubble_images[3]

        elif sell == "P":
            return self.bubble_images[4]

        elif sell == "B":
            return self.bubble_images[-1]

    def add_bubble_into_group(self, map):
        for row_idx, row in enumerate(map):
            for col_idx, sell in enumerate(row):
                if sell in [".", "/"]:
                    continue

                self.add_bubble(row_idx, col_idx, sell)

    def add_bubble(self, row_idx, col_idx, sell):
        position = self.get_bubble_position(row_idx, col_idx)
        image = self.get_bubble_image(sell)
        self.bubble_group.add(Bubble(image, sell, position))

    def get_bubble_group(self):
        return self.bubble_group


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = Screen().set_screen()
        self.images = Image()
        self.map = Map(self.images.get_bubbles())
        self.bubbles = Bubble_Group(self.images.get_bubbles())
        self.pointer = Pointer(self.images.get_pointer())
        self.total_angle = 0

    def set_game_loop(self):
        self.map.setup()
        while self.running:
            self.set_frame_rate()
            self.bubbles.add_bubble_into_group(self.map.get_map())
            self.screen.blit(self.images.get_background(), (0, 0))
            
            self.manage_events()
            self.pointer.rotate(self.total_angle)
            self.bubbles.get_bubble_group().draw(self.screen)
            self.pointer.draw(self.screen)
            pygame.display.update()
        
    def set_frame_rate(self):
        frame_rate = 60
        self.clock.tick(frame_rate)

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.total_angle += ANGLE_SPEED

                elif event.key == pygame.K_RIGHT:
                    self.total_angle -= ANGLE_SPEED
                
            elif event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.total_angle = 0








    
def main():
    pygame.init()

    game = Game()
    game.set_game_loop()
            
    pygame.quit()


    
if __name__ == "__main__":
    main()