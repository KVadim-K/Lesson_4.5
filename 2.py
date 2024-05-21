import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Настройки экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Размеры экрана
pygame.display.set_caption("Tetris")

# Основной класс игры
class Tetris:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.shapes = [
            [[1, 1, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 0, 0], [1, 1, 1]],
            [[0, 0, 1], [1, 1, 1]],
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]],  # Крест
        ]
        self.colors = [CYAN, YELLOW, MAGENTA, GREEN, RED, BLUE, ORANGE]
        self.current_shape = random.choice(self.shapes)
        self.current_color = random.choice(self.colors)
        self.current_x = 3
        self.current_y = 0

# **Метод рисования игрового поля**
# Рисует игровое поле на экране.
    def draw_board(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                color = WHITE if self.board[y][x] == 0 else self.colors[self.board[y][x] - 1]
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# **Метод рисования фигуры**
# Рисует фигуру на игровом поле.
    def draw_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[y])):
                if self.current_shape[y][x] != 0:
                    pygame.draw.rect(screen, self.current_color, ((self.current_x + x) * BLOCK_SIZE, (self.current_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, BLACK, ((self.current_x + x) * BLOCK_SIZE, (self.current_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# **Метод поворота фигуры**
# Поворачивает фигуру на 90 градусов по часовной стрелке.
    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]
# **Метод проверки допустимости позиции фигуры**
# Проверяет, можно ли разместить фигуру в новой позиции, не выходя за границы игрового поля
# и не сталкиваясь с другими фигурами.
    def is_valid_position(self, shape, offset_x, offset_y):
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x] != 0:
                    new_x = self.current_x + x + offset_x
                    new_y = self.current_y + y + offset_y
                    if new_x < 0 or new_x >= len(self.board[0]) or new_y >= len(self.board):
                        return False
                    if new_y >= 0 and self.board[new_y][new_x] != 0:
                        return False
        return True

# #**Метод размещения текущей фигуры на доске**
# Размещает текущую фигуру на доске, очищает заполненные линии
# и генерирует новую фигуру.
    def place_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[y])):
                if self.current_shape[y][x] != 0:
                    self.board[self.current_y + y][self.current_x + x] = self.colors.index(self.current_color) + 1
        self.clear_lines()
        self.new_shape()

# **Метод очистки заполненных линий**
# Удаляет полностьюзаполненные линии и добавляет очки за каждую линию.
    def clear_lines(self):
        lines_to_clear = [index for index, row in enumerate(self.board) if all(row)]
        for index in lines_to_clear:
            del self.board[index]
            self.board.insert(0, [0 for _ in range(10)])
        self.score += len(lines_to_clear) ** 2

# **Методы генерации новой фигуры**
# Создает новую фигуру и проверяет, можно ли ее разместить на доске.
# Если она вдруг не может быть размещена то игра окончена
    def new_shape(self):
        self.current_shape = random.choice(self.shapes)
        self.current_color = random.choice(self.colors)
        self.current_x = 3
        self.current_y = 0
        if not self.is_valid_position(self.current_shape, 0, 0):
            self.game_over()

# **Метод окончания игры**
# Окончание игры, если фигура не может быть размещена на доске.
    def game_over(self):
        self.__init__()
        print("Game Over")

# **Метод перемещения фигуры**
# Перемещает фигуру влево или вправо, если она может быть размещена.
    def move(self, dx, dy):
        if self.is_valid_position(self.current_shape, dx, dy):
            self.current_x += dx
            self.current_y += dy
        elif dy != 0:
            self.place_shape()

# **Метод падения фигуры**
# Падает фигуру вниз, если она может быть размещена.
    def drop(self):
        while self.is_valid_position(self.current_shape, 0, 1):
            self.current_y += 1
        self.place_shape()

# **Метод перемещения фигуры вниз**
# Перемещает фигуру вниз, если она может быть размещена.
    def update(self):
        self.move(0, 1)

# Основная функция игры
# Запуск игры
# Отрисовка доски
# Отрисовка текущей фигуры
# Обновление доски
# Обновление текущей фигуры
def main():
    clock = pygame.time.Clock()
    game = Tetris()
    running = True
    drop_event = pygame.USEREVENT + 1
    pygame.time.set_timer(drop_event, 1000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == drop_event:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                if event.key == pygame.K_DOWN:
                    game.move(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate_shape()
                if event.key == pygame.K_SPACE:
                    game.drop()

        screen.fill(BLACK)
        game.draw_board()
        game.draw_shape()
        pygame.display.flip()
        clock.tick(30)


    pygame.quit()

if __name__ == '__main__':
    main()