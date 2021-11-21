from solar_objects import Star, Planet

from solar_vis import DrawableObject



def read_space_objects_data_from_file(solar_system):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:
    **input_filename** — имя входного файла
    """
    objects = []
    with open(solar_system.txt, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue 
            object_type = line.split()[0].lower()
            if object_type == "star":
                """Класс Star"""
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")
    input_file.close()
    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считываем данные о звезде из строки.
       Формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
       Параметры:
    **line** — строка с описанием звезды.
    **star** — объект звезды."""
    
    w_list = line.split()
    star.R = int(w_list[1])
    star.color = w_list[2].lower()
    star.m = float(w_list[3])
    star.x = float(w_list[4])
    star.y = float(w_list[5])
    star.Vx = float(w_list[6])
    star.Vy = float(w_list[7])
    pass  


def parse_planet_parameters(line, planet):
    """Считываем данные о планете из строки.
       Формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
       Параметры:
    **line** — строка с описанием планеты.
    **planet** — объект планеты."""
    
    w_list = line.split()
    planet.R = int(w_list[1])
    planet.color = w_list[2].lower()
    planet.m = float(w_list[3])
    planet.x = float(w_list[4])
    planet.y = float(w_list[5])
    planet.Vx = float(w_list[6])
    planet.Vy = float(w_list[7])
    pass


def write_space_objects_data_to_file(solar_system, space_objects):
    """Сохраняем данные о космических объектах в файл."""
    
    with open(solar_system.txt, 'w') as out_file:
        for obj in space_objects:
            print("%s %d %s %e %e %e %e %e\n" % (obj.obj.type,
                                                 obj.obj.R,
                                                 obj.obj.color,
                                                 obj.obj.m,
                                                 obj.obj.x,
                                                 obj.obj.y,
                                                 obj.obj.Vx,
                                                 obj.obj.Vy))
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

