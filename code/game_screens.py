import pygame
from initial_variables import variables
from load_assets import background, main_font, sub_font, round_track, background_track, score_track, key_press, key_press_fail
from game_logic import display_new_stratagem, render_static_elements, display_stratagem_queue, input_display, create_progress_bar
from round_manager import start_round_timer, round_timeout, reset_round_timer

window = pygame.display.set_mode((variables.WIDTH, variables.HEIGHT))

def start_screen():
    window.blit(background, (0, 0))
    title = main_font.render("STRATAGEM HERO", 1, variables.WHITE)
    subtitle = sub_font.render("Enter any Stratagem Input to Start!", 1, variables.YELLOW)
    window.blit(title, (variables.WIDTH / 2 - title.get_width() / 2, variables.HEIGHT / 2.7))
    window.blit(subtitle, (variables.WIDTH / 2 - subtitle.get_width() / 2, variables.HEIGHT / 1.49))
    pygame.display.update()
    
def round_screen(round_count, stratagems_per_round, score_count):
    
    if round_count > 1:
       
        round_track.play()
        
    start_time = pygame.time.get_ticks()
    remaining_time = variables.round_time_limit
    run = True
    while run:
        window.blit(background, (0, 0))
        round_title = main_font.render("GET READY", 1, variables.WHITE)
        round_subtitle = sub_font.render("Round", 1, variables.WHITE)
        round_number = sub_font.render(str(round_count), 1, variables.YELLOW)
        window.blit(round_title, (variables.WIDTH / 2 - round_title.get_width() / 2, variables.HEIGHT / 2.7))
        window.blit(round_subtitle, (variables.WIDTH / 2 - round_subtitle.get_width() / 2, variables.HEIGHT / 1.54))
        window.blit(round_number, (variables.WIDTH / 2 - round_number.get_width() / 2, variables.HEIGHT / 1.42))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False

        if pygame.time.get_ticks() - start_time > 1500:
            game_screen(round_count, stratagems_per_round, remaining_time, score_count)
            return False
        
def score_window(round_count, stratagems_per_round, score_count, current_remaining_time, perfect_round):
    
    score_track.play()
    
    start_time = pygame.time.get_ticks()
    run = True

    bonuses = [
        ("Round Bonus", 75 + (round_count - 2) * 25),
        ("Time Bonus", round(current_remaining_time * 10)),
        ("Perfect Bonus", 100 if perfect_round else 0),
        ("Total Score", score_count + 75 + (round_count - 2) * 25 + round(current_remaining_time * 10) + (100 if perfect_round else 0))
    ]

    score_count = bonuses[-1][1]

    while run:
        current_time = pygame.time.get_ticks()
        window.blit(background, (0, 0))

        for i, (label, score) in enumerate(bonuses):
            if current_time - start_time > i * 1000:
                text = sub_font.render(label, 1, variables.WHITE)
                number = sub_font.render(str(score), 1, variables.YELLOW)
                window.blit(text, (200, 400 + i * 100))
                window.blit(number, (variables.WIDTH - 400 - number.get_width(), 400 + i * 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False

        if current_time - start_time > 4000:
            round_screen(round_count, stratagems_per_round, score_count)
            return False
        
def game_screen(round_count, stratagems_per_round, remaining_time, score_count):
    
    background_track.play()
   
    stratagem_categories, stratagems_for_round, icons_for_round = display_new_stratagem(stratagems_per_round)
    stratagem = stratagems_for_round[0]
    user_input = []
    input_index = 0
    incorrect_input = False
    perfect_round = True
    flash_time = 0
    completed_stratagems = 0
    start_time = pygame.time.get_ticks()
    
    run = True
    while run:
        current_remaining_time = start_round_timer(remaining_time, start_time)
        colour = variables.RED if current_remaining_time <= 2 else variables.YELLOW
        
        window.blit(background, (0, 0))
        render_static_elements(window, stratagem, round_count, score_count, colour)  
        display_stratagem_queue(window, icons_for_round)
        input_display(window, stratagem, input_index, incorrect_input)
        
        create_progress_bar(window, current_remaining_time, colour)
        pygame.display.update()

        if current_remaining_time <= 0:
            background_track.stop()
            from main import main
            round_timeout(window, background, score_count, main_font, sub_font, variables.WHITE, variables.YELLOW, variables.WIDTH, variables.HEIGHT, main)
            return False

        if incorrect_input and pygame.time.get_ticks() - flash_time > 200:
            incorrect_input = False
            user_input = []
            input_index = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    user_input.append('up')
                elif event.key == pygame.K_DOWN:
                    user_input.append('down')
                elif event.key == pygame.K_LEFT:
                    user_input.append('left')
                elif event.key == pygame.K_RIGHT:
                    user_input.append('right')

                if user_input and user_input[input_index] == stratagem.inputs[input_index]:
                    
                    key_press.set_volume(0.2)
                    key_press.play()
                    input_index += 1
                else:
                    
                    key_press_fail.set_volume(0.2)
                    key_press_fail.play()
                    incorrect_input = True
                    perfect_round = False
                    flash_time = pygame.time.get_ticks()

                if len(user_input) == len(stratagem.inputs) and user_input == stratagem.inputs:
                    completed_stratagem_length = len(stratagem.inputs)
                    remaining_time = reset_round_timer(current_remaining_time, completed_stratagem_length)
                    
                    score_count += completed_stratagem_length * 5
                    
                    user_input = []
                    input_index = 0
                    completed_stratagems += 1
                    if completed_stratagems < stratagems_per_round:
                        if icons_for_round:
                            icons_for_round.pop(0)
                        stratagem = stratagems_for_round[completed_stratagems]
                    start_time = pygame.time.get_ticks()

                    if completed_stratagems >= stratagems_per_round:
                        background_track.stop()
                        round_count += 1
                        stratagems_per_round += 1
                        completed_stratagems = 0
                        score_window(round_count, stratagems_per_round, score_count, current_remaining_time, perfect_round)
                        return False

        pygame.display.update()