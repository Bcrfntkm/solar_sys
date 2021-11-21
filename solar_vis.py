import pygame as pg

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

colors = {'red': 0xFF0000, 'blue': 0x0000FF,
          'yellow': 0xFFC91, 'green': 0x00FF00,
          'magenta': 0xFF03B8, 'cyan': 0x00FFCC,
          'black': 0, 'white': 0xFFFFFF,
          'orange': 0xFFA500, 'gray': 0x7D7D7D}

header_font = "Arial-16"  # Шрифт в заголовке
window_width = 1000  # Ширина окна
window_height = 900  # Высота окна
scale_factor = 1  # Масштабирование экранных координат по отношению к физическим.


# Тип: float      Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """
    Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине
    """
    global scale_factor
    scale_factor = 0.5 * min(window_height, window_width) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    global scale_factor
    return int(x * scale_factor) + window_width / 2


def scale_y(y):
    global scale_factor
    return int(y * scale_factor) + window_height / 2


if __name__ == "__main__":
    print("This module is not for direct call!")



class Drawer:
    """
    Выводим на экран figure из массива figures[] и меню
    """

    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, menu):
        self.screen.fill((0, 0, 0))
        # отрисовка всех объектов
        for figure in figures:
            figure.draw(self.screen)

        # отрисовка и отображение
        menu.blit_and_update()
        pg.display.update()


class DrawableObject:
    def __init__(self, obj):
        self.obj = obj
        # переводим слово в число через словарь
        # если цвета нет, тогда серый цвет
        self.obj.color = colors.get(self.obj.color, 'gray')
        self.obj.rV = []
        self.obj.En = []

    def draw(self, surface):
        x = scale_x(self.obj.x)
        y = scale_y(self.obj.y)
        pg.draw.circle(
            surface,
            self.obj.color,
            (x, window_height - y),
            self.obj.R)
