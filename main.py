import pygame
from Life import Life


if __name__ == '__main__':
    pygame.init()
    # n = int(input("n: "))
    n = 20
    live = Life(n, n)
    size = width, height = live.left * 2 + live.cell_size*n , live.top * 2 + live.cell_size*n
    screen = pygame.display.set_mode(size)
    running = True
    stop = True
    fps = 5
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    live.get_click(event.pos)
                if event.button == 3:
                    stop = not stop
                if event.button == 4:
                    fps += 1
                if event.button == 5:
                    fps -= 1
            if event.type == 769:
                stop = not stop
        screen.fill((0, 0, 0))
        if not stop:
            live.next_move()
        live.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.display.flip()
    pygame.quit()