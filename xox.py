import pygame
import sys

# Pygame ayarları
pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (255, 255, 255)
CIRCLE_COLOR = (242, 85, 96)
CROSS_COLOR = (28, 170, 156)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Ekranı oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XOX Oyunu")
screen.fill(BG_COLOR)

# XOX oyunu tahtası
board = [[None] * 3 for _ in range(3)]
current_player = "X"

# Tahta çizim fonksiyonu
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

# X çizen fonksiyon
def draw_cross(row, col):
    pygame.draw.line(screen, CROSS_COLOR, (col * 100 + SPACE, row * 100 + SPACE),
                     (col * 100 + 100 - SPACE, row * 100 + 100 - SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (col * 100 + SPACE, row * 100 + 100 - SPACE),
                     (col * 100 + 100 - SPACE, row * 100 + SPACE), CROSS_WIDTH)

# O çizen fonksiyon
def draw_circle(row, col):
    pygame.draw.circle(screen, CIRCLE_COLOR, (col * 100 + 50, row * 100 + 50), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Kazananı kontrol etme fonksiyonu
def check_win(player):
    # Satır ve sütun kontrolü
    for row in range(3):
        if all([spot == player for spot in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Çapraz kontrol
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Tıklama pozisyonunu tahtaya çevirme fonksiyonu
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col

draw_lines()

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            row, col = get_row_col_from_mouse(pos)

            # Geçerli boş kutuya tıklanıp tıklanmadığını kontrol et
            if board[row][col] is None:
                board[row][col] = current_player

                # X veya O çiz
                if current_player == "X":
                    draw_cross(row, col)
                    if check_win("X"):
                        print("X Kazandı!")
                        running = False
                else:
                    draw_circle(row, col)
                    if check_win("O"):
                        print("O Kazandı!")
                        running = False

                # Sırayı değiştir
                current_player = "O" if current_player == "X" else "X"

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
