import pygame
import sys

pygame.init()

# === Game Settings ===
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Team Rocket: New Island Heist - Text Adventure")

FONT = pygame.font.SysFont("Arial", 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# === Scene Data ===
# Placeholder backgrounds are just colors; gadgets are colored boxes
scenes = [
    {
        "bg_color": (50, 100, 200),
        "text": "Jessie spots a rare Gyarados near the docks! Which gadget will help catch it?",
        "gadgets": ["Gadget A", "Gadget B", "Gadget C"],
        "correct": 1,
        "fail_text": "Oh no! The gadget backfired and scared it away!"
    },
    {
        "bg_color": (100, 50, 200),
        "text": "James finds a powerful Alakazam guarding the gate. What will you use?",
        "gadgets": ["Gadget A", "Gadget B", "Gadget C"],
        "correct": 0,
        "fail_text": "The gadget fizzled! Alakazam teleported you back."
    },
    {
        "bg_color": (200, 50, 50),
        "text": "Meowth sees Mewtwo's shadow in the lab. Pick your final gadget wisely!",
        "gadgets": ["Gadget A", "Gadget B", "Gadget C"],
        "correct": 2,
        "fail_text": "Mewtwo wasn’t impressed. Team Rocket is blasting off again!"
    }
]

current_scene = 0
message = ""
game_over = False

def draw_scene(scene_index, message=""):
    scene = scenes[scene_index]
    
    # Background
    screen.fill(scene["bg_color"])

    # Draw text box
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 150, WIDTH, 150))
    
    # Scene text
    wrapped = wrap_text(scene["text"], FONT, WIDTH - 20)
    for i, line in enumerate(wrapped):
        txt_surface = FONT.render(line, True, WHITE)
        screen.blit(txt_surface, (10, HEIGHT - 140 + i * 28))
    
    # Message (fail text)
    if message:
        msg_surface = FONT.render(message, True, WHITE)
        screen.blit(msg_surface, (10, HEIGHT - 40))

    # Draw gadgets as clickable boxes
    for i, gadget in enumerate(scene["gadgets"]):
        rect = pygame.Rect(150 + i * 200, HEIGHT // 2 - 50, 150, 100)
        pygame.draw.rect(screen, (200, 200 - i*50, 50 + i*60), rect)
        g_txt = FONT.render(gadget, True, BLACK)
        screen.blit(g_txt, (rect.centerx - g_txt.get_width()//2, rect.centery - g_txt.get_height()//2))

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines, current_line = [], ""
    for word in words:
        test_line_
