import pygame
import os
import random
from initial_variables import variables

def load_arrow_images():
    arrow_grey = pygame.image.load(os.path.join('assets', 'images', 'arrow_grey.png'))

    up_image = pygame.transform.rotate(arrow_grey, 90)
    down_image = pygame.transform.rotate(arrow_grey, -90)
    left_image = pygame.transform.rotate(arrow_grey, 180)
    right_image = arrow_grey

    arrow_yellow = pygame.image.load(os.path.join('assets', 'images', 'arrow_yellow.png'))

    up_image_true = pygame.transform.rotate(arrow_yellow, 90)
    down_image_true = pygame.transform.rotate(arrow_yellow, -90)
    left_image_true = pygame.transform.rotate(arrow_yellow, 180)
    right_image_true = arrow_yellow
    
    arrow_red = pygame.image.load(os.path.join('assets', 'images', 'arrow_red.png'))

    up_image_false = pygame.transform.rotate(arrow_red, 90)
    down_image_false = pygame.transform.rotate(arrow_red, -90)
    left_image_false = pygame.transform.rotate(arrow_red, 180)
    right_image_false = arrow_red

    return {
        'up': up_image,
        'down': down_image,
        'left': left_image,
        'right': right_image,
        'up_true': up_image_true,
        'down_true': down_image_true,
        'left_true': left_image_true,
        'right_true': right_image_true,
        'up_false': up_image_false,
        'down_false': down_image_false,
        'left_false': left_image_false,
        'right_false': right_image_false
    }


def icon_select(category, selected_stratagem):
    
    icon = pygame.image.load(os.path.join('assets', category, selected_stratagem.icon))
    
    return icon

#background image   
background = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'super_earth.png')), (variables.WIDTH, variables.HEIGHT))
  
#fonts  
pygame.font.init()

main_font = pygame.font.Font(os.path.join('assets', 'Fonts', 'autobahn_stencil.ttf'), 132)
sub_font = pygame.font.Font(os.path.join('assets', 'Fonts', 'autobahn.ttf'), 58)

#audio
pygame.mixer.init()

start = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Start.mp3'))
round_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Round Track.mp3'))
background_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Background Track.mp3'))
track_number = random.randint(1, 4)
score_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', f'Score Track {track_number}.mp3'))
key_press = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'key_press.mp3'))
key_press_fail = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'key_press_fail.mp3'))
game_over = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Game Over.mp3'))

#highscores

high_scores_file = (os.path.join('assets', 'highscores' , 'highscores.txt'))
    
      