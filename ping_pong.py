from pygame import *

# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
BALL_X = 150
BALL_Y = 100



# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))

# название окна
display.set_caption("ping-pong")


# задать картинку фона такого же размера, как размер окна
background = transform.scale(
    image.load("стол.png"),
    # здесь - размеры картинки
    (WIN_W, WIN_H)
)

ball = transform.scale(
    image.load('мяч.png'),
    # здесь - размеры картинки
    (BALL_X, BALL_Y)
)


# игровой цикл
game = True
while game:
    # отобразить картинку фона
    window.blit(background,(0, 0))
    window.blit(ball,(100, 100))
    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
