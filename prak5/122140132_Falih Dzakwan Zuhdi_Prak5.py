import pygame
import sys

pygame.init()

screen_size = 300
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Tic Tac Toe')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Board:
    def __init__(self):
        self.cells = [['' for _ in range(3)] for _ in range(3)]

    def draw(self):
        for y in range(3):
            for x in range(3):
                rect = pygame.Rect(x*100, y*100, 100, 100)
                pygame.draw.rect(screen, WHITE, rect, 1)
                if self.cells[y][x] != '':
                    font = pygame.font.SysFont(None, 124)
                    img = font.render(self.cells[y][x], True, WHITE)
                    screen.blit(img, (x*100 + 30, y*100 + 10))

    def update_cell(self, x, y, player):
        if self.cells[y][x] == '':
            self.cells[y][x] = player
            
    def check_winner(self):
        for row in self.cells:
            if row[0] == row[1] == row[2] != '':
                return row[0]

        for col in range(3):
            if self.cells[0][col] == self.cells[1][col] == self.cells[2][col] != '':
                return self.cells[0][col]

        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != '':
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != '':
            return self.cells[0][2]

        return None

def update_screen(board):
    screen.fill(BLACK)
    board.draw()
    pygame.display.flip()

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board, x, y):
        board.update_cell(x, y, self.symbol)

board = Board()
player_x = Player('X')
player_o = Player('O')
current_player = player_x

running = True
winner = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            x, y = pygame.mouse.get_pos()
            x //= 100
            y //= 100
            current_player.make_move(board, x, y)
            winner = board.check_winner()
            current_player = player_o if current_player == player_x else player_x
    update_screen(board)

    if winner:
        print(f"Pemenangnya adalah: {winner}")
        running = False

