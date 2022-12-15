import os
import pygame
import random
import math

CURRENT_PATH = os.path.dirname(__file__)
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
SCREEN_WIDTH = 448
SCREEN_HEIGHT = 720
MAP_ROW = 11
MAP_COL = 8

ANGLE_SPEED = 0.1
MAX_RIGHT_ANGLE = 10
MAX_LEFT_ANGLE = 170
POINTER_POSITION = (SCREEN_WIDTH // 2, 624)
NEXT_BUBBLE_POSITION = (26, 720 - 31)
BUBBLE_SPEED = 0.7
FPS = 60

RED = 0
YELLOW = 1
BLUE = 2
GREEN = 3
PURPLE = 4
BLACK = -1


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

    def get_bubble_of(self, color):
        return self.bubble_images[color]
    
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

class Game_Object(pygame.sprite.Sprite):
    def __init__(self, image) -> None:
        super().__init__()
        self.image = image
        self.rect = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Pointer(Game_Object):
    def __init__(self, image):
        super().__init__(image)
        self.original_image = image
        self.rect = image.get_rect(center=POINTER_POSITION)
        self.angle = 90
        self.left_difference_of_angle = 0
        self.right_difference_of_angle = 0

    def move_left_direction(self):
        self.left_difference_of_angle += ANGLE_SPEED

    def move_right_direction(self):
        self.right_difference_of_angle -= ANGLE_SPEED

    def stop_left_direction(self):
        self.left_difference_of_angle = 0

    def stop_right_direction(self):
        self.right_difference_of_angle = 0

    def rotate(self, df):
        self.angle = self.angle + (self.right_difference_of_angle + self.left_difference_of_angle) * df
        if self.angle <= MAX_RIGHT_ANGLE:
            self.angle = MAX_RIGHT_ANGLE 

        elif self.angle >= MAX_LEFT_ANGLE:
            self.angle = MAX_LEFT_ANGLE 

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=POINTER_POSITION)

    def get_angle(self):
        return self.angle

class Bubble(Game_Object):
    def __init__(self, image, color:str, position=(0,0)):
        super().__init__(image)
        self.color = color
        self.rect = image.get_rect(center=position)

    def set_rect(self, position):
        self.rect = self.image.get_rect(center=position)

    def set_angle(self, angle):
        self.angle = angle
        self.rad_angle = math.radians(self.angle)
        
    def move(self, df):
        difference_x = BUBBLE_SPEED * math.cos(self.rad_angle)
        difference_y = -BUBBLE_SPEED * math.sin(self.rad_angle)

        self.rect.x += difference_x * df
        self.rect.y += difference_y * df

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH: 
            self.set_angle(180 - self.angle)

    def is_movement_end(self):
        return self.rect.bottom < 0

class Map:
    def __init__(self) -> None:
        self.map = []
        self.colors = []

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
        
        self.set_colors()

    def get_map(self):
        return self.map

    def get_colors(self):
        return self.colors

    def set_colors(self):
        self.colors = []
        for row in self.map:
            for col in row:
                if col not in self.colors and col not in [".", "/"]:
                    self.colors.append(col)

    def set_map(self, row_idx, col_idx, color):
        self.map[row_idx][col_idx] = color


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

    def add_current_bubble(self, bubble):
        self.bubble_group.add(bubble)

    def get_bubble_group(self):
        return self.bubble_group


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen = Screen().set_screen()
        self.images = Image()
        self.map = Map()
        self.bubbles = Bubble_Group(self.images.get_bubbles())
        self.pointer = Pointer(self.images.get_pointer())
        self.current_bubble = None
        self.next_bubble = None
        self.fire = False

    def set_game_loop(self):
        self.map.setup()
        self.bubbles.add_bubble_into_group(self.map.get_map())
        while self.running:
            self.df = self.set_frame_rate()
            self.map.set_colors()
            self.manage_events()

            self.revolve_bubble()
            
            self.collision_manage()

            self.draw_screen()

            self.draw_pointer()

            self.draw_current_bubble()
            self.draw_next_bubble()

            if self.current_bubble.is_movement_end():
                self.delete_current_bubble()

            pygame.display.update()
        
    def set_frame_rate(self):
        frame_rate = FPS
        return self.clock.tick(frame_rate)

    def revolve_bubble(self):
        if not self.current_bubble:
            self.prepare_current_bubble()
        if not self.next_bubble:
            self.prepare_next_bubble()

    def draw_screen(self):
        self.screen.blit(self.images.get_background(), (0, 0))
        self.bubbles.get_bubble_group().draw(self.screen)

    def draw_pointer(self):
        self.pointer.rotate(self.df)
        self.pointer.draw(self.screen)

    def draw_current_bubble(self):
        if self.current_bubble:
            if self.fire:
                self.current_bubble.move(self.df)
            self.current_bubble.draw(self.screen)

    def draw_next_bubble(self):
        if self.next_bubble:
            self.next_bubble.draw(self.screen)

    def delete_current_bubble(self):
            self.current_bubble = self.next_bubble
            self.current_bubble.set_rect(POINTER_POSITION)
            self.next_bubble = self.prepare_next_bubble()
            self.fire = False

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.pointer.move_left_direction()

                elif event.key == pygame.K_RIGHT:
                    self.pointer.move_right_direction()

                elif event.key == pygame.K_SPACE:
                    if self.current_bubble and not self.fire:
                        self.fire_bubble()
                
            elif event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.pointer.stop_left_direction()

                if event.key == pygame.K_RIGHT:
                    self.pointer.stop_right_direction()

    def fire_bubble(self):
        self.fire = True
        self.current_bubble.set_angle(self.pointer.get_angle())

    def prepare_current_bubble(self):
        self.current_bubble = self.create_bubble(POINTER_POSITION)

    def prepare_next_bubble(self):
        self.next_bubble = self.create_bubble(NEXT_BUBBLE_POSITION)

    def create_bubble(self, position):
        color = self.get_random_color()
        image = self.images.get_bubble_of(self.number_of(color))
        return Bubble(image, color, position)
    
    def get_random_color(self):
        return random.choice(self.map.get_colors())

    def number_of(self, color):
        if color == "R":
            return RED
        elif color == "Y":
            return YELLOW
        elif color == "B":
            return BLUE
        elif color == "G":
            return GREEN
        elif color == "P":
            return PURPLE

    def collision_manage(self):
        if self.fire:
            hit_bubble = pygame.sprite.spritecollideany(self.current_bubble, self.bubbles.get_bubble_group(), pygame.sprite.collide_mask)
            if hit_bubble:
                row_idx, col_idx = self.get_map_index(*self.current_bubble.rect.center)
                self.place_bubble(row_idx, col_idx)
                
    def get_map_index(self, x, y):
        row_idx = y // CELL_SIZE
        col_idx = x // CELL_SIZE
        if row_idx % 2 == 1:
            col_idx = (x - (CELL_SIZE // 2)) // CELL_SIZE

            if col_idx < 0:
                col_idx = 0
            if col_idx > MAP_COL - 2:
                col_idx = MAP_COL - 2

        return row_idx, col_idx

    def place_bubble(self, row_idx, col_idx):
        self.map.set_map(row_idx, col_idx, self.current_bubble.color)
        position = self.bubbles.get_bubble_position(row_idx, col_idx)
        self.current_bubble.set_rect(position)
        self.bubbles.add_current_bubble(self.current_bubble)
        self.delete_current_bubble()




    
def main():
    pygame.init()

    game = Game()
    game.set_game_loop()
            
    pygame.quit()


    
if __name__ == "__main__":
    main()