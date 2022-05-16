import pygame

# Initialize pygame and the screen
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 14)
clock = pygame.time.Clock() # frame rate
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Mouse events')

def update_text(text, color=(0, 255, 255)):
    text = text.encode()
    mf = myfont.render(text, True, color)
    screen.blit(mf, (10, 10))


def main():
    c = 0
    tc = (c,c,c)
    text = "'http://pythonprogramming.altervista.org'"
    color = (255,255,255)
    update_text(text, color=color)
    loop = 1
    CORAL = (128,0,0)
    DARKGREEN = (0,255,128)
    COLOR = CORAL
    while loop:
        screen.fill(COLOR)
        clock.tick(60)
        events = pygame.event.get()
        update_text(text, color=color)
        for event in events:
            if event.type == pygame.QUIT:
                loop = 0
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action, color = "pressed", (0,255, 255)
                if event.type == pygame.MOUSEBUTTONUP:
                    action, color = "released", (255, 64, 64)
                if event.button == 4:
                    print("MOUSEWHEEL UP")
                    action = "MOUSEWHEEL UP"
                    COLOR = CORAL
                if event.button == 5:
                    print("MOUSEWHEEL DOWN")
                    action = "MOUSEWHEEL DOWN"
                    COLOR = DARKGREEN


                text = f'button {event.button} {action} in the position {event.pos}'
                print(text)
        pygame.display.update()
    pygame.quit()

main()