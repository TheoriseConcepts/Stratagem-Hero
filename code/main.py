import pygame
from initial_variables import variables
from game_screens import start_screen, round_screen
from load_assets import start

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(variables.FPS)
        start_screen()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    
                    start.play()
                    
                    run = round_screen(variables.round_count, variables.stratagems_per_round, variables.score_count)

        if not run:
            break

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()