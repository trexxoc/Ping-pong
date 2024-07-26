from pygame import *

# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
BALL_X = 120
BALL_Y = 85
RACKET_ONEX = 150
RACKET_ONEY = 150
RACKET_TWOX = 127
RACKET_TWOY = 150



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


racket1 = transform.scale(
    image.load('player1.png'),
    # здесь - размеры картинки
    (RACKET_ONEX, RACKET_ONEY)
)


racket2 = transform.scale(
    image.load('player2.png'),
    # здесь - размеры картинки
    (RACKET_TWOX, RACKET_TWOY)
)



# игровой цикл
game = True
while game:
    # отобразить картинку фона
    window.blit(background,(0, 0))
    window.blit(ball,(290, 205))
    window.blit(racket1,(0, 150))
    window.blit(racket2,(550, 150))

    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()


