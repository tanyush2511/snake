import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204,255,255)
size = [400, 600]
COUNT_BLOKS = 20
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()

    screen.fill(FRAME_COLOR)

    for column in range(COUNT_BLOKS):
        if column%2 == 0:
            color == BLUE
        else:
            color == WHITE
        pygame.draw.rect(screen, color, [10 + column*SIZE_BLOCK, 20, SIZE_BLOCK, SIZE_BLOCK])


    pygame.display.flip()
