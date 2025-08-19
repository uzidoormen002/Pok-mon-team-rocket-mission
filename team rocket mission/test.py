import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team rockets biggest catch secret mission")

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Characters
team_rocket = ["NARRATOR"]
current_speaker = 0

dialogue = [
    ("NARRATOR", "Hello I’m the narrator of the pokemon universe you have been chosen"),
    ("NARRATOR", "to redeem the past failures of Jessie James and Meowth from team rocket")
    ("NARRATOR", "from a cutrain point of time you will have to chose the actions Jessie James and Meowth have to take to redeem themselfs"),
    ("NARRATOR", "to do this you wil be sent to new island"),
    ("NARRATOR", "Hey! What are you creeps doing here?!"),
    ("NARRATOR", "We’re here to, uh, admire the Pokémon... totally not steal them!"),
    ("NARRATOR", "Pika pii!"),
    ("NARRATOR", "Even the Pikachu knows we’re lying..."),
    ("NARRATOR", "You dare trespass on my island? Your ambition will be your downfall."),
    ("NARRATOR", "Uh-oh..."),
]

dialogue_index = 0

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Draw current dialogue
    if dialogue_index < len(dialogue):
        speaker, line = dialogue[dialogue_index]
        text_surface = font.render(f"{speaker}: {line}", True, WHITE)
        screen.blit(text_surface, (50, HEIGHT - 100))
    else:
        text_surface = font.render("End of Demo. To be continued...", True, WHITE)
        screen.blit(text_surface, (50, HEIGHT - 100))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dialogue_index += 1  # Move to next line of dialogue

    clock.tick(30)

pygame.quit()
sys.exit()