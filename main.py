import pygame

pygame.init()
screen = pygame.display.set_mode((600,100))
pygame.display.set_caption("Stopwatch")

class Stopwatch:
    def __init__(self, screen):
        self.screen = screen
        self.ms = 0
        self.seconds = 0
        self.minutes = 0
        self.current_time = "0:0:0"
        self.font = pygame.font.SysFont("comicsans", 64)
        self.stop = False
        self.CLOCK_STOPPED = self.font.render("STOPPED", False, (255,255,))

    def stop_clock(self):
        if self.stop:
            self.stop = False
        else:
            self.stop = True


    def update_clock(self):
        if not self.stop:
            self.ms += 1
            if self.ms % 60 == 0:
                self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
        self.current_time = self.font.render(f"{self.minutes}:{self.seconds}:{self.ms % 60}", False, (255,255,255))

    def show_clock(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.current_time, (236,0))
        if self.stop:
            self.screen.fill((255,0,0))
            self.screen.blit(self.CLOCK_STOPPED, ((600 - self.CLOCK_STOPPED.get_width() )//2, 0))

    def update_stopwatch(self):
        self.update_clock()
        self.show_clock()


run = True
clock = pygame.time.Clock()
s = Stopwatch(screen)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s.stop_clock()
    s.update_stopwatch()
    pygame.display.update()