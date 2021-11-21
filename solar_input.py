from solar_objects import *
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:
    **input_filename** — имя входного файла
    """
    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            # расщепляем строку на слова и первое слово lowercase
            object_type = line.split()[0].lower()
            if object_type == "star" or object_type == "planet":
                # создаём объект класса Body
                body = Body()
                # считываем данные из строки и заполняем объект
                parse_body_parameters(line, body)
                # загоняем объект в массив объектов
                objects.append(body)
            else:
                print("Unknown space object")
    input_file.close()
    # превращаем объект класса Body в Drawable
    return [DrawableObject(obj) for obj in objects]


def parse_body_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описанием звезды.
    **star** — объект звезды.
    """
    global Sm
    w_list = line.split()
    star.type = w_list[0].lower()
    star.R = int(w_list[1])
    star.color = w_list[2].lower()
    star.m = float(w_list[3])
    if star.type == "star":
        Sm = star.m
        print(Sm)
    star.x = float(w_list[4])
    star.y = float(w_list[5])
    star.Vx = float(w_list[6])
    star.Vy = float(w_list[7])
    #    star.rV.clear()
    #   star.En.clear()


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write("%s %d %s %e %e %e %e %e\n" % (obj.obj.type,
                                                          obj.obj.R,
                                                          obj.obj.color,
                                                          obj.obj.m,
                                                          obj.obj.x,
                                                          obj.obj.y,
                                                          obj.obj.Vx,
                                                          obj.obj.Vy))

    out_file.close()


if __name__ == "__main__":
    print("This module is not for direct call!")
