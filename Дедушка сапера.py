import pygame, random

pygame.init()
screen = pygame.display.set_mode((500, 500))
class Minesweeper:
    # создание поля
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        s = []
        for _ in range(mines):
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            while [x, y] in s:
                x = random.randint(0, height - 1)
                y = random.randint(0, width - 1)
            print(x, y)
            s.append([x, y])
            self.board[x][y] = 10
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.flag = False
        self.red_x = -1
        self.red_y = -1
        self.mines = mines

    def render(self):
        colors = {10: pygame.Color('red'), -1: pygame.Color('black')}
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] in [10, -1]:
                    pygame.draw.rect(screen,
                                     colors[self.board[y][x]],
                                     (self.left + self.cell_size * x,
                                      self.top + self.cell_size * y,
                                      self.cell_size,
                                      self.cell_size))
                    pygame.draw.rect(screen,
                                     pygame.Color('white'),
                                     (self.left + self.cell_size * x,
                                      self.top + self.cell_size * y,
                                      self.cell_size,
                                      self.cell_size), 1)
                else:
                    text_x = (self.left + self.cell_size * x) + 10
                    text_y = (self.top + self.cell_size * y) + 10
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(self.board[y][x]), 1, (100, 255, 100))
                    screen.blit(text, (text_x - 5, text_y - 5))
                    pygame.draw.rect(screen,
                                     pygame.Color('white'),
                                     (self.left + self.cell_size * x,
                                      self.top + self.cell_size * y,
                                      self.cell_size,
                                      self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        print(cell_x, cell_y)
        return cell_x, cell_y

    def on_click(self, cell):
        x = cell[0]
        y = cell[1]
        self.open_cell(x, y)

    def open_cell(self, x, y):
        if self.board[y][x] != 10:
            count = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= j <= self.height - 1 and 0 <= i <= self.width - 1 and not (i == x and j == y):
                            if self.board[j][i] == 10:
                                count += 1
            self.board[y][x] = count

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

board = Minesweeper(8, 8, 8)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()