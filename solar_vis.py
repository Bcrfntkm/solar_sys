import pygame as pg

"""Модуль визуализации, использующий экранные координаты объекта.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

red = 0xFF0000
blue = 0x0000FF
yellow = 0xFFC91
green = 0x00FF00
magenta = 0xFF03B8
cyan = 0x00FFCC
black = 0
white = 0xFFFFFF
orange = 0xFFA500
gray = 0x7D7D7D

colors = {  'red': red,
            'blue': blue,
            'yellow': yellow,
            'green': green,
            'magenta': magenta,
            'cyan': cyan,
            'black': black,
            'white': white,
            'orange': orange,
            'gray': gray
                                }

header_font = "Arial-16"  """Шрифт в заголовке"""
window_width = 1000  
window_height = 900  
scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим"""





def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
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




"""Выводим на экран figure из массива figures[] и меню"""

class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, menu):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            figure.draw(self.screen)

        menu.blit_and_update()
        pg.display.update()
        
"""Отрисовка всех объектов и их отображение"""



"""Взаимодействуем со словарем цветов"""

class DrawableObject:
    def __init__(self, obj):
        self.obj = obj
        self.color = colors.get(self.obj.color, gray)

    def draw(self, surface):
        x = scale_x(self.obj.x)
        y = scale_y(self.obj.y)
        pg.draw.circle(
            surface,
            self.color,
            (x, window_height - y),
            self.obj.R)
