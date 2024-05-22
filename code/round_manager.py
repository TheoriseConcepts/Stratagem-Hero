import pygame
import os
from initial_variables import variables
from load_assets import game_over, high_scores_file

def start_round_timer(remaining_time, start_time):
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    current_remaining_time = remaining_time - elapsed_time
    return current_remaining_time

def reset_round_timer(remaining_time, completed_stratagem_length):
    remaining_time += 0.1 * completed_stratagem_length
    remaining_time = min(remaining_time, variables.round_time_limit)
    return remaining_time


def load_high_scores(file_path):
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    scores = []
    for line in lines:
        name, score = line.strip().split(',')
        scores.append((name, int(score)))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:3]

def save_high_scores(file_path, scores):
    with open(file_path, 'w') as file:
        for name, score in scores:
            file.write(f"{name},{score}\n")

def get_player_name(window, background, main_font, sub_font, WHITE, YELLOW, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    input_box = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2, 200, 60)
    color_active = pygame.Color('yellow')
    color = color_active
    active = True
    text = ''
    done = False
    max_chars = 24
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < max_chars:
                        text += event.unicode

        window.blit(background, (0, 0))
        name_prompt_text = main_font.render("New High Score!", True, WHITE)
        window.blit(name_prompt_text, (WIDTH / 2 - name_prompt_text.get_width() / 2, 350))
        name_prompt_text = sub_font.render("Enter your name:", True, WHITE)
        window.blit(name_prompt_text, (WIDTH / 2 - name_prompt_text.get_width() / 2, 525))
        
        txt_surface = sub_font.render(text, True, WHITE)
        width = max(200, txt_surface.get_width() + 25)  # Ensure some padding around text
        input_box.w = width
        input_box.center = (WIDTH / 2, HEIGHT / 2 + 100)  # Keep the input box centered
        
        vertical_padding = (input_box.height - txt_surface.get_height()) // 2
        window.blit(txt_surface, (input_box.x + (input_box.w - txt_surface.get_width()) // 2, input_box.y + vertical_padding))
        pygame.draw.rect(window, color, input_box, 2)
        
        pygame.display.flip()
        clock.tick(30)
    
    return text

def check_and_update_high_scores(window, background, main_font, sub_font, WHITE, YELLOW, WIDTH, HEIGHT, file_path, score_count):
    scores = load_high_scores(file_path)
    if len(scores) < 3 or score_count > scores[-1][1]:
        name = get_player_name(window, background, main_font, sub_font, WHITE, YELLOW, WIDTH, HEIGHT)
        scores.append((name, score_count))
        scores.sort(key=lambda x: x[1], reverse=True)
        save_high_scores(file_path, scores[:3])

def round_timeout(window, background, score_count, main_font, sub_font, WHITE, YELLOW, WIDTH, HEIGHT, restart_callback):
    
    game_over.play()
    run = True
    
    check_and_update_high_scores(window, background, main_font, sub_font, WHITE, YELLOW, WIDTH, HEIGHT, high_scores_file, score_count)
    high_scores = load_high_scores(high_scores_file)
    
    start_time = pygame.time.get_ticks()
    
    while run:
        window.blit(background, (0, 0))
        round_text_a = main_font.render("GAME OVER", 1, WHITE)
        round_text_b = sub_font.render("High Scores", 1, WHITE)
        round_text_c = sub_font.render("Your Final Score", 1, WHITE)
        round_text_d = sub_font.render(str(score_count), 1, YELLOW)
        
        window.blit(round_text_a, (WIDTH / 2 - round_text_a.get_width() / 2, 175))
        window.blit(round_text_b, (WIDTH / 2 - round_text_b.get_width() / 2, 325))
        
        # Display the high scores
        for i, (name, score) in enumerate(high_scores):
            high_score_text = sub_font.render(f"{i + 1}. {name} | {score}", 1, WHITE)
            window.blit(high_score_text, (WIDTH / 2 - high_score_text.get_width() / 2, 400 + i * 75))
        
        window.blit(round_text_c, (WIDTH / 2 - round_text_c.get_width() / 2, 700))
        window.blit(round_text_d, (WIDTH / 2 - round_text_d.get_width() / 2, 775))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False
            
        if pygame.time.get_ticks() - start_time > 5000:
            run = False
            restart_callback()
            
    pygame.quit()