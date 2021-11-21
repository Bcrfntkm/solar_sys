# coding: utf-8
# license: GPLv3
class Body():
    """Тип данных, описывающий небесное тело.
    Содержит массу, координаты, скорость тела,
    а также визуальный радиус тела в пикселах и её цвет.
    """

    def __init__(self):
        self.type = type  # "star/planet"   # Признак объекта звезды

        self.R = 5  # Радиус звезды
        self.color = "red"  # Цвет звезды
        self.m = 1  # Масса звезды
        self.x = y = 0  # Координаты по оси x y
        self.Vx = Vy = 0  # Скорость по оси x y
        self.Fx = Fy = 0  # Силы по оси x y
