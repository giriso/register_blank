import pygame
import copy

pygame.init()
size = 350, 450
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
my_event = 31
pygame.time.set_timer(my_event, 50)


# размеры окна:
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 10

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        colors = [pygame.Color('white'), pygame.Color('black')]
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, colors[1],
                                 (self.left + self.cell_size * i,
                                  self.top + self.cell_size * j,
                                  self.cell_size, self.cell_size), 1)
                pygame.draw.ellipse(screen,
                                    colors[self.board[j][i]],
                                    (self.left + self.cell_size * i + 1,
                                     self.top + self.cell_size * j + 1,
                                     self.cell_size - 2, self.cell_size - 2), 0)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell):
        self.board[cell[1]][cell[0]] = (self.board[cell[1]][cell[0]] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def next_move(self):
        t_board = copy.deepcopy(self.board)
        for i in range(self.width):
            for j in range(self.height):
                x1, y1 = i - 1, j - 1
                x2, y2 = i + 1, j + 1
                if x1 < 0:
                    x1 = self.width - 1
                if y1 < 0:
                    y1 = self.height - 1
                if x2 == self.width:
                    x2 = 0
                if y2 == self.height:
                    y2 = 0

                neighbours = sum([self.board[y1][i], self.board[y2][i],
                                  self.board[j][x1], self.board[j][x2],
                                  self.board[y1][x1], self.board[y1][x2],
                                  self.board[y2][x1], self.board[y2][x2]])
                if self.board[j][i] == 0 and neighbours == 3:
                    t_board[j][i] = 1
                elif self.board[j][i] == 1 and (neighbours < 2 or neighbours > 3):
                    t_board[j][i] = 0
        self.board = copy.deepcopy(t_board)


board = Life(20, 20)
flag = False
num = 0
speed = 8
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flag = not flag
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            flag = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            speed += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            speed -= 1
        if event.type == my_event and flag:
            board.next_move()
    if speed < 1:
        speed = 1
    screen.fill((255, 255, 255))
    board.render()
    pygame.display.flip()
    clock.tick(speed)

# завершение работы:
pygame.quit()
