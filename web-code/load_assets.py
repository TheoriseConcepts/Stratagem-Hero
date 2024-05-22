import pygame
import os
import random
import time
from initial_variables import variables


arrow_grey = pygame.image.load(os.path.join('assets', 'Images', 'arrow_grey.png'))
arrow_yellow = pygame.image.load(os.path.join('assets', 'Images', 'arrow_yellow.png'))
arrow_red = pygame.image.load(os.path.join('assets', 'Images', 'arrow_red.png'))

arrow_images = {
    'up': pygame.transform.rotate(arrow_grey, 90),
    'down': pygame.transform.rotate(arrow_grey, -90),
    'left': pygame.transform.rotate(arrow_grey, 180),
    'right': arrow_grey,
    'up_true': pygame.transform.rotate(arrow_yellow, 90),
    'down_true': pygame.transform.rotate(arrow_yellow, -90),
    'left_true': pygame.transform.rotate(arrow_yellow, 180),
    'right_true': arrow_yellow,
    'up_false': pygame.transform.rotate(arrow_red, 90),
    'down_false': pygame.transform.rotate(arrow_red, -90),
    'left_false': pygame.transform.rotate(arrow_red, 180),
    'right_false': arrow_red
    }


def icon_select(category, selected_stratagem):
    
    icon = pygame.image.load(os.path.join('assets', category, selected_stratagem.icon))
    
    return icon

#background image   
background = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Images', 'super_earth.png')), (variables.WIDTH, variables.HEIGHT))
  
#fonts  
pygame.font.init()

main_font = pygame.font.Font(os.path.join('assets', 'Fonts', 'autobahn_stencil.ttf'), 132)
sub_font = pygame.font.Font(os.path.join('assets', 'Fonts', 'autobahn.ttf'), 58)

#audio
#pygame.mixer.init()

start = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Start.ogg'))
round_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Round Track.ogg'))
background_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Background Track.ogg'))

def select_score_track():

    current_time = int(time.time())
    random.seed(current_time)
    track_number = random.randint(1, 4)
    score_track = pygame.mixer.Sound(os.path.join('assets', 'Audio', f'Score Track {track_number}.ogg'))
    
    return score_track

key_press_load = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'key_press.ogg'))
key_press_load.set_volume(0.2)
key_press = key_press_load
key_press_fail_load = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'key_press_fail.ogg'))
key_press_fail_load.set_volume(0.2)
key_press_fail = key_press_fail_load
game_over = pygame.mixer.Sound(os.path.join('assets', 'Audio', 'Game Over.ogg'))

#highscores

high_scores_file = (os.path.join('assets', 'Highscores' , 'highscores.txt'))
    
      