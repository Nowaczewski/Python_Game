import pygame

def main ():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
    #poll for events
    #pygame.Quit() event means the user clicked x to close out your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #fill the screen with a color to wipe away anything from the Last Frame
        screen.fill((0,255,255))

        #Render game here:

        # Flip() the display to put your work on screen
        pygame.display.flip()

        #limit to 60 FPS
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()