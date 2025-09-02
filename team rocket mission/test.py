import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("team rockets biggest catch mission")


font = pygame.font.SysFont("Arial", 24)


WHITE = (210, 100, 0)
BLACK = (10, 60, 160)
yellow = (240, 217, 9)

background = pygame.image.load("https://www.bing.com/images/search?view=detailV2&ccid=AMhKDord&id=5E9D5DD4087B209F1DDC8AA8AC1A2930E8AF14EC&thid=OIP.AMhKDordlB0tTufTM9q8DQHaER&mediaurl=https%3a%2f%2fstatic.wikia.nocookie.net%2fpokemon%2fimages%2f2%2f23%2f787549_M22_Logo_EN_wPokemon_Dark_Final.jpg%2frevision%2flatest%2fscale-to-width-down%2f1200%3fcb%3d20200228165144&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.00c84a0e8add941d2d4ee7d333dabc0d%3frik%3d7BSv6DApGqyoig%26pid%3dImgRaw%26r%3d0&exph=693&expw=1200&q=mewtwo+strikes+back+evolution&FORM=IRPRST&ck=75851BCC29F5A7A5A648C440569432B1&selectedIndex=24&itb=0")
background = pygame.transform.scale("https://www.bing.com/images/search?view=detailV2&ccid=AMhKDord&id=5E9D5DD4087B209F1DDC8AA8AC1A2930E8AF14EC&thid=OIP.AMhKDordlB0tTufTM9q8DQHaER&mediaurl=https%3a%2f%2fstatic.wikia.nocookie.net%2fpokemon%2fimages%2f2%2f23%2f787549_M22_Logo_EN_wPokemon_Dark_Final.jpg%2frevision%2flatest%2fscale-to-width-down%2f1200%3fcb%3d20200228165144&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.00c84a0e8add941d2d4ee7d333dabc0d%3frik%3d7BSv6DApGqyoig%26pid%3dImgRaw%26r%3d0&exph=693&expw=1200&q=mewtwo+strikes+back+evolution&FORM=IRPRST&ck=75851BCC29F5A7A5A648C440569432B1&selectedIndex=24&itb=0", (WIDTH, HEIGHT))

team_rocket = ["NARRATOR" "Jessie" "James" "Meowth"]
current_speaker = 0

dialogue = [
    ("NARRATOR", "Hello I’m the narrator of the pokemon universe you have been chosen"),
    ("NARRATOR", "to live through the past failures of Jessie James and Meowth"),
    ("NARRATOR", "from a cutrain point of time you will have to chose the actions of"),
    ("NARRATOR", "Jessie James and Meowth to redeem themselfs"),
    ("NARRATOR", "to do this you wil be sent to new island"),
    ("NARRATOR", "your mission is to capture all the pokemon on the island"),
    ("NARRATOR", "or at least some of the pokemon on the island you choose which"),
    ("NARRATOR", "and if you can capture Mewtwo but it will be difficult to do"),
    ("NARRATOR", "when your ready just press space when the button begin pops up"),
    ("NARRATOR", "the controls are arrows and to comfirm an option press space"),
    ("NARRATOR", "good luck team rocket HAHAHA!!!"),
]

dialogue_index = 0


clock = pygame.time.Clock()


while True:
    screen.blit(background, (0, 0))


    if dialogue_index < len(dialogue):
        speaker, line = dialogue[dialogue_index]
        text_surface = font.render(f"{speaker}: {line}", True, WHITE)
        screen.blit(text_surface, (50, HEIGHT - 100))
    else:
        text_surface = font.render("you have failed, better luck next time or not HAHAHAHA!!!", True, WHITE)
        screen.blit(text_surface, (50, HEIGHT - 100))



    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dialogue_index += 1  

    clock.tick(30)

pygame.quit()
sys.exit()