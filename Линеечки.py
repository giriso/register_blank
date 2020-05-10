import pygame


screen = pygame.display.set_mode((500, 500))
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.flag = False
        self.red_x = -1
        self.red_y = -1

    def render(self):
        colors = [pygame.Color('black'), pygame.Color('blue'), pygame.Color('red'), pygame.Color('orange')]
        for x in range(self.width):
            for y in range(self.height):
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
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        print(cell_x, cell_y)
        return cell_x, cell_y

    def neighbours(self, start, end):
        board = self.board
        if start[0] == end[0] and start[1] == end[1]:
            return True
        st_y = start[0]
        st_x = start[1]
        end_y = end[0]
        end_x = end[1]
        else:
            for x in range(self.width):
                for y in range(self.height):

        n_y = y - 1
        n_x = x - 1
        for i in range(3):
            if 0 <= n_y <= self.height - 1:
                continue
            for j in range(3):
                if 0 <= n_x <= self.width - 1:
                    continue
                    board

    def on_click(self, cell):
        x = cell[0]
        y = cell[1]
        if not self.flag:
            self.board[y][x] = (self.board[y][x] + 1) % 3
        else:
            self.board[y][x] = 1
            self.flag = False
            self.board[self.red_y][self.red_x] = 0
            self.red_x = -1
            self.red_y = -1
        if self.board[y][x] == 2:
            self.flag = True
            self.red_x = x
            self.red_y = y
            print(self.flag)


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

board = Board(5, 7)
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