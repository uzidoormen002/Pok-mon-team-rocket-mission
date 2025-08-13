import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team rockets biggest catch secret mission")

def main():
    global current_level, game_state, selected_items

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == "level":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if current_level < total_levels:
                        game_state = "item_select"
                        selected_items = []
                    else:
                        print("Game Over!")
                        pygame.quit()
                        sys.exit()

            elif game_state == "item_select":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    for rect, item in item_buttons:
                        if rect.collidepoint(mx, my):
                            if item in selected_items:
                                selected_items.remove(item)
                            elif len(selected_items) < 3:
                                selected_items.append(item)

                if len(selected_items) == 3:
                    current_level += 1
                    game_state = "level"

        if game_state == "level":
            draw_level_screen(current_level)
        elif game_state == "item_select":
            draw_item_selection()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
("Hello I'm the narrator of the pokemon universe you have been chosen to redeem the failures that Jessie James and Meowth from a curtain point in time sneak onto the island controled by Mewtwo to redeem them to redeem them you must choose the actions Jessie James and Meowth take to try and steal all the pokemon on New island top priority is capture Mewtwo if you can't then you can secondary objective is to capture other pokemon click begin when ready good luck hahahaha!!!")

