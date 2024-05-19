import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size) #создание окна
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("image.png") #загрузка изображения
image_rect = image.get_rect() #Создаём переменную для хитбокса

image2 = pygame.image.load("image2.png")
image_rect2 = image2.get_rect()

speed = 1

run = True

while run: #создания игрового цикла создаём переменную и задаём цикл:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed
    if event.type == pygame.MOUSEMOTION: #получаем координаты мыши
        mouse_x, mouse_y = event.pos #получаем координаты мыши
        image_rect.x = mouse_x - (image_rect.width / 2) # передаем координаты мыши по центру
        image_rect.y = mouse_y - (image_rect.height / 2) # передаем координаты мыши по центру

    if image_rect.colliderect(image_rect2): #проверка на столкновение
        print("Змея съела мышь")
        time.sleep(1)

    screen.fill((0, 0, 0)) #задаём цвет
    screen.blit(image, image_rect) #добавляем персонажа после screen.fill
    screen.blit(image2, image_rect2) #добавляем 2-го персонажа

    pygame.display.flip() #обновляем экран и видим изменения на экране

pygame.quit()