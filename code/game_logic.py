import pygame
import random
from initial_variables import variables
from stratagems import Stratagems
from load_assets import icon_select, background, sub_font, load_arrow_images

def display_new_stratagem(stratagems_per_round):
    stratagem_categories = list(Stratagems.keys())
    stratagem_category = []
    stratagems_for_round = []
    icons_for_round = []

    for _ in range(stratagems_per_round):
        category = random.choice(stratagem_categories)
        stratagem_category.append(category)
        all_stratagems = Stratagems[category]
        selected_stratagem = random.choice(all_stratagems)
        stratagems_for_round.append(selected_stratagem)
        icon = icon_select(category, selected_stratagem)
        icons_for_round.append(icon) 

    return stratagem_categories, stratagems_for_round, icons_for_round

def running_score(window, score, text_color):
    score_text_dynamic = sub_font.render("Score", 1, variables.WHITE)
    score_number_dynamic = sub_font.render(str(score), 1, text_color)
    window.blit(score_text_dynamic, (variables.WIDTH / 1.15 - score_text_dynamic.get_width(), variables.HEIGHT / 4.8))
    window.blit(score_number_dynamic, (variables.WIDTH / 1.15 - score_number_dynamic.get_width(), variables.HEIGHT / 6.17))

def render_static_elements(window, stratagem, round_count, score, colour):
    window.blit(background, (0, 0))
    round_text_static = sub_font.render("Round", 1, variables.WHITE)
    round_number_static = sub_font.render(str(round_count), 1, colour)
    pygame.draw.rect(window, colour, (480, 246, 250, 250), 5)
    stratagem_name_text = sub_font.render(stratagem.name, 1, variables.BLACK)
    text_rect = stratagem_name_text.get_rect(center=(variables.WIDTH / 2, variables.HEIGHT / 2.06))
    rect_width, rect_height = variables.WIDTH / 2, text_rect.height + 10
    rect_x, rect_y = (variables.WIDTH - rect_width) / 2, text_rect.y
    pygame.draw.rect(window, colour, (rect_x, rect_y, rect_width, rect_height))
    window.blit(stratagem_name_text, text_rect)
    window.blit(round_text_static, (variables.WIDTH / 12.8 + round_text_static.get_width()/2, variables.HEIGHT / 6.17))
    window.blit(round_number_static, (variables.WIDTH / 6.4 + round_number_static.get_width()/2, variables.HEIGHT / 4.8))
    running_score(window, score, colour)
     
def display_stratagem_queue(window, icons_for_round):
    icon_x, icon_y = variables.WIDTH / 3.84, variables.HEIGHT / 3.93
    
    num_icons = min(len(icons_for_round), 6)
    
    for i in range(num_icons):
        icon_index = i
        if i == 0:
            icon = pygame.transform.scale(icons_for_round[icon_index], (variables.large_icon_size, variables.large_icon_size))
            window.blit(icon, (icon_x, icon_y))
            current_x = icon_x + variables.large_icon_size + variables.icon_spacing
        else:
            icon = pygame.transform.scale(icons_for_round[icon_index], (variables.small_icon_size, variables.small_icon_size))
            window.blit(icon, (current_x, icon_y + 50 ))
            current_x += variables.small_icon_size + variables.icon_spacing
            
def input_display(window, stratagem, input_index, incorrect_input):
    arrow_images = load_arrow_images()
    input_start_pos = variables.WIDTH / 2 - (len(stratagem.inputs) * arrow_images['right'].get_width()) // 2
    for i, input in enumerate(stratagem.inputs):
        if i < input_index:
            if incorrect_input:
                arrow_image = arrow_images[input + '_false']
            else:
                arrow_image = arrow_images[input + '_true']
        else:
            arrow_image = arrow_images[input]
        window.blit(arrow_image, (input_start_pos, variables.HEIGHT / 1.74))
        input_start_pos += variables.small_icon_size     
        
def create_progress_bar(window, remaining_time, colour):
    BAR_WIDTH, BAR_HEIGHT = variables.WIDTH / 2, variables.HEIGHT / 36
    BAR_X, BAR_Y = (variables.WIDTH - BAR_WIDTH) // 2, variables.HEIGHT / 1.32
    pygame.draw.rect(window, variables.GREY, (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(window, colour, (BAR_X, BAR_Y, BAR_WIDTH * (remaining_time / variables.round_time_limit), BAR_HEIGHT))
            
