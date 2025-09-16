import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team rockets biggest catch mission")

font = pygame.font.SysFont("Arial", 24)

WHITE = (210, 100, 0)
BLACK = (10, 60, 160)
YELLOW = (240, 217, 9)

intro_dialogue = [
    ("NARRATOR", "Hello I’m the narrator of the pokemon universe you have been chosen"),
    ("NARRATOR", "to live through the past failures of Jessie James and Meowth"),
    ("NARRATOR", "from a cetrain point of time you will have to chose the actions of"),
    ("NARRATOR", "Jessie James and Meowth to redeem themselves"),
    ("NARRATOR", "to do this you will be sent to new island"),
    ("NARRATOR", "your mission is to capture all the pokemon on the island"),
    ("NARRATOR", "or at least some of the pokemon on the island you choose which"),
    ("NARRATOR", "and if you can capture Mewtwo then great an expiriment returned"),
    ("NARRATOR", "the controls are arrows and to comfirm an option press space"),
    ("NARRATOR", "good luck hopefully you don’t blast off HAHAHA!!!"),
    ("NARRATOR", "so yeah when your ready just press space to start the mission"),
]

staircase_dialogue = [
    ("Jessie", "Look James, a spiral staircase leading into the tower!"),
    ("James", "Do we really have to climb this? I just polished my boots."),
    ("Meowth", "Stop complainin’! There could be rare Pokémon at the top!"),
    ("NARRATOR", "You begin climbing the spiral staircase... step by step."),
    ("NARRATOR", "The air grows colder, and you hear the echo of a Pokémon cry above."),
]

mainland_dialogue = [
    ("Jessie", "I don’t trust this island. Let’s swim back to the mainland."),
    ("James", "But Jessie, I left my inflatable Arbok at HQ!"),
    ("Meowth", "You two are hopeless..."),
    ("NARRATOR", "Despite the bickering, you dive into the water and start paddling."),
    ("NARRATOR", "A school of Water Pokémon follows, curious about your mission."),
]

underwater_dialogue = [
    ("Jessie", "Maybe there’s something under the waves. Let’s check."),
    ("James", "I hope my hair gel is waterproof..."),
    ("Meowth", "Quit yappin’ and start swimmin’!"),
    ("NARRATOR", "You dive below, finding ruins covered in strange carvings."),
    ("NARRATOR", "running out of breath as you go deeper you see a air pocket."),
    ("NARRATOR", "entering the air pocket you see a strange pokemon hovering"),
    ("NARRATOR", "in the centre of the air pocket levating water and rocks"),
    ("NARRATOR", "the pokemon notices you and it being curious it flys at you"),
    ("James", "get this weird tiny rat away from me it stearing at me")
]

pokemon_battle_dialogue = [
    ("NARRATOR", "The ground shakes. A bright light pierces the sky."),
    ("Jessie", "What in the world is that?!"),
    ("James", "Those aren’t ordinary Pokémon..."),
    ("Meowth", "No way... they’re fightin’ their own clones!"),
    ("NARRATOR", "On the battlefield, Pikachu faces its clone, refusing to strike back."),
    ("Jessie", "This... this is too cruel, even for Team Rocket."),
    ("NARRATOR", "Charizard and its clone clash, their roars shaking the tower."),
    ("James", "I can’t tell who’s the real one anymore!"),
    ("NARRATOR", "Mewtwo hovers above, watching as the chaos unfolds."),
    ("Meowth", "If dis keeps up... there won’t be any pokemon left to steal!"),
]

dialogue_index = 0
displayed_text = ""
char_index = 0
typing_speed = 2
finished_line = False

clock = pygame.time.Clock()

START_SCREEN = 0
INTRO = 1
ADVENTURE_PROMPT = 2
CHOICE_MENU = 3
STAIRCASE = 4
MAINLAND = 5
UNDERWATER = 6
POKEMON_BATTLE = 7
state = START_SCREEN

choices = ["Go up the spiral staircase", "Swim back to the mainland", "Look underwater for clues"]
selected_choice = 0

def draw_text_center(text, y, color=WHITE):
    surf = font.render(text, True, color)
    screen.blit(surf, (WIDTH//2 - surf.get_width()//2, y))

def handle_dialogue(dialogue_list):
    global dialogue_index, char_index, displayed_text, finished_line
    if dialogue_index < len(dialogue_list):
        speaker, line = dialogue_list[dialogue_index]
        if not finished_line:
            char_index += typing_speed
            displayed_text = line[:char_index]
            if char_index >= len(line):
                displayed_text = line
                finished_line = True
        text_surface = font.render(f"{speaker}: {displayed_text}", True, WHITE)
        screen.blit(text_surface, (50, HEIGHT - 100))
        return False
    else:
        return True  

running = True
while running:
    screen.fill(BLACK)

    if state == START_SCREEN:
        draw_text_center("Team Rocket’s Biggest Catch Mission", HEIGHT//2 - 50, YELLOW)
        draw_text_center("Press SPACE to Begin", HEIGHT//2 + 20, WHITE)

    elif state == INTRO:
        if handle_dialogue(intro_dialogue):
            state = ADVENTURE_PROMPT

    elif state == ADVENTURE_PROMPT:
        draw_text_center("Start Adventure", HEIGHT//2, YELLOW)
        draw_text_center("(Press SPACE to continue)", HEIGHT//2 + 40, WHITE)

    elif state == CHOICE_MENU:
        draw_text_center("Choose your action:", HEIGHT//4, YELLOW)
        for i, choice in enumerate(choices):
            color = YELLOW if i == selected_choice else WHITE
            draw_text_center(choice, HEIGHT//2 + i*40, color)

    elif state == STAIRCASE:
        if handle_dialogue(staircase_dialogue):
            state = POKEMON_BATTLE
            dialogue_index, displayed_text, char_index, finished_line = 0, "", 0, False

    elif state == MAINLAND:
        if handle_dialogue(mainland_dialogue):
            state = POKEMON_BATTLE
            dialogue_index, displayed_text, char_index, finished_line = 0, "", 0, False

    elif state == UNDERWATER:
        if handle_dialogue(underwater_dialogue):
            state = POKEMON_BATTLE
            dialogue_index, displayed_text, char_index, finished_line = 0, "", 0, False

    elif state == POKEMON_BATTLE:
        if handle_dialogue(pokemon_battle_dialogue):
            draw_text_center("To be continued... The battle rages on!", HEIGHT//2, YELLOW)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == START_SCREEN:
                if event.key == pygame.K_SPACE:
                    state = INTRO

            elif state in [INTRO, STAIRCASE, MAINLAND, UNDERWATER, POKEMON_BATTLE]:
                dialogue_map = {
                    INTRO: intro_dialogue,
                    STAIRCASE: staircase_dialogue,
                    MAINLAND: mainland_dialogue,
                    UNDERWATER: underwater_dialogue,
                    POKEMON_BATTLE: pokemon_battle_dialogue,
                }
                dialogue_list = dialogue_map[state]
                if event.key == pygame.K_SPACE:
                    if not finished_line:
                        _, line = dialogue_list[dialogue_index]
                        displayed_text = line
                        char_index = len(line)
                        finished_line = True
                    else:
                        dialogue_index += 1
                        displayed_text = ""
                        char_index = 0
                        finished_line = False

            elif state == ADVENTURE_PROMPT:
                if event.key == pygame.K_SPACE:
                    state = CHOICE_MENU

            elif state == CHOICE_MENU:
                if event.key == pygame.K_UP:
                    selected_choice = (selected_choice - 1) % len(choices)
                elif event.key == pygame.K_DOWN:
                    selected_choice = (selected_choice + 1) % len(choices)
                elif event.key == pygame.K_SPACE:
                    if selected_choice == 0:
                        state = STAIRCASE
                    elif selected_choice == 1:
                        state = MAINLAND
                    elif selected_choice == 2:
                        state = UNDERWATER
                    dialogue_index, displayed_text, char_index, finished_line = 0, "", 0, False

    clock.tick(30)

pygame.quit()
sys.exit()
