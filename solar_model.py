# coding: utf-8
# license: GPLv3

G = gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def force(A, B):
    """
    Функция рассчитывает гравитационное взамодействие между телами (объектами) А и В
    """
    # расстояния между телами по осям
    dx = B.x - A.x
    dy = B.y - A.y
    # расстояние между телами
    r = (dx * dx + dy * dy) ** 0.5
    # модуль силы
    F = G * A.m * B.m / r / r
    # обработка деления на 0
    if dx != 0:
        tg = dy / dx
        if tg < 0: tg = -tg
        Fx = F / ((tg * tg + 1) ** 0.5)
        Fy = Fx * tg
    else:
        Fy = F
        Fx = 0
    # модули сил определены, теперь знаки
    if dy < 0:        Fy = -Fy
    if dx < 0:        Fx = -Fx
    # добавляем силы к уже приложенным к телам
    A.Fx += Fx
    A.Fy += Fy
    B.Fx -= Fx
    B.Fy -= Fy


# рассчитываем все взаимные влияниия сил
def calculate_forces(space_objects):
    # обнуляем все силы на всех телах
    for i in space_objects:
        i.Fx = i.Fy = 0
    # требуется перебрать все пары по одному разу
    for i in range(len(space_objects)):  # 012345
        for j in range(i + 1, len(space_objects)):
            # обрабатываем пару объектов
            force(space_objects[i],
                  space_objects[j])
    pass


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        r = max(r, body.R)
        pass


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.
    Параметры:
    **body** — тело, которое нужно переместить.
    """
    old = body.x
    # ускорения по осям
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    # скорости по осям
    body.Vx += ax * dt
    body.Vy += ay * dt
    # перемещения по осям
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.
    Параметры:
    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """
    calculate_forces(space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
