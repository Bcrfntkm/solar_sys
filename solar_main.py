# coding: utf-8
# license: GPLv3

import pygame as pg
import time
import numpy as np

import thorpy  # GUI for pygame
from thorpy import functions

from solar_vis import *
from solar_model import *
from solar_input import *
from solar_objects import *

# timer_text = None
alive = True
perform_execution = False  # Флаг цикличности выполнения расчёта"""
model_time = 0  # """Физическое время от начала расчёта.Тип: float"""
time_scale = 3600.0  # """Шаг по времени при моделировании.  Тип: float"""
space_objects = []  # """Список космических объектов."""
# берём параметры экрана из модуля solar_vis
width = window_width  # 1000
height = window_height  # 900

button_play = None
menu = None
browserlauncher = None
drawer = None
FPS = 60
save_name = None


def execution(delta):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global model_time
    global displayed_time
    recalculate_space_objects_positions([dr.obj for dr in space_objects], delta)
    model_time += delta


# -----------------------------Pause
def pause_execution():
    global perform_execution
    perform_execution = True
    start_execution()


"""Обработчик события нажатия на кнопку Start.Запускает циклическое исполнение функции execution."""


# -----------------------------Play/Pause
def start_execution():
    global perform_execution
    global button_play
    perform_execution = not perform_execution
    if perform_execution:
        button_play.set_text('Pause')
    else:
        button_play.set_text('Play')
    """ корректируем размер кнопки"""
    button_play.scale_to_title()


# -----------------------------open file
def stop_execution():  # """Обработчик события нажатия на кнопку Start.Останавливает циклическое исполнение функции execution."""
    global alive
    alive = False


# -----------------------------open file
def open_file():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global model_time
    global browserlauncher
    #    global drawer
    """ останавливаем выполнение на период загрузки"""
    # pause_execution()

    in_filename = browserlauncher.var_text
    if in_filename != "":
        # in_filename="solar_system.txt"
        model_time = 0.0
        """ имя файла задано статически"""
        # in_filename = "solar_system.txt"
        """ создаём список(массив) объектов солнечной системы"""
        space_objects = read_space_objects_data_from_file(in_filename)
        """ определяем расстояние между самыми удалёнными объектами"""
        max_distance = max([max(abs(obj.obj.x), abs(obj.obj.y)) for obj in space_objects])
        """ для корректного отображения на экране определяем соотношение между экраном и солнечной системой"""
        calculate_scale_factor(max_distance)


# -----------------------------save file
def save_file():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global model_time
    global browserlauncher
    global save_name
    """останавливаем выполнение на период загрузки"""
    pause_execution()
    out_filename = save_name.get_value()
    print(out_filename)
    if out_filename != "":
        """ создаём список(массив) объектов солнечной системы"""
        write_space_objects_data_to_file(out_filename, space_objects)


# ---------------------------------------------handle events
def handle_events(events, menu):
    global alive
    for event in events:
        menu.react(event)

        if event.type == pg.QUIT:
            alive = False


# -----------------------------slider reaction
def slider_to_real(val):
    return np.exp(5 + val)


def slider_reaction(event):
    global time_scale
    time_scale = slider_to_real(event.el.get_value())


# -----------------------------init menu
def init_ui(screen):
    global button_play
    global browserlauncher
    global save_name

    slider = thorpy.SliderX(100, (-10, 10), "Simulation speed")
    slider.user_func = slider_reaction
    """ создаём кнопки и привязываем их к процедурам"""
    button_stop = thorpy.make_button('Quit', func=stop_execution)
    button_pause = thorpy.make_button('Pause', func=pause_execution)
    button_play = thorpy.make_button('Play', func=start_execution)
    button_load = thorpy.make_button(text='Load a file', func=open_file)
    button_save = thorpy.make_button(text='save a file', func=save_file)

    browser = thorpy.Browser(file_types=['.txt'], text='Browser', folders=True)
    browserlauncher = thorpy.BrowserLauncher(browser, const_text='file:')
    browserlauncher.max_chars = 40  # limit size of browser launcher
    browserlauncher.scale_to_title()

    timer_text = thorpy.OneLineText("days passed")
    save_name = thorpy.Inserter(name="SaveName: ", value="MyState.txt")
    box = thorpy.Box(elements=[
        browserlauncher,
        button_load,
        button_play,
        slider,
        save_name,
        button_save,
        button_stop,
        #    button_pause,
        timer_text])

    # фильтр событий для слайдера
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    box.add_reaction(reaction1)

    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((0, 0))
    ##    box.blit()
    ##    box.update()
    functions.set_current_menu(menu)
    return menu, box, timer_text


# ------------------------------------------------------------main
def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global perform_execution
    global timer_text
    global screen
    global menu
    global drawer

    print('Modelling started!')
    physical_time = 0

    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()

    last_time = time.perf_counter()
    # создаём экземпляр 
    drawer = Drawer(screen)  # vis.py
    menu, box, timer_text = init_ui(screen)
    perform_execution = False
    #   drawer.update(space_objects,menu) #vis.py

    while alive:
        # обработка событий от пользовательского меню
        menu.react_to_all_events()
        # handle_events(pg.event.get(), menu)

        cur_time = time.perf_counter()
        if perform_execution:
            execution((cur_time - last_time) * time_scale)  # 1000
            text = "%d days passed" % (int(model_time / 3600 / 24))
            timer_text.set_text(text)
        last_time = cur_time
        clock.tick(FPS)
        drawer.update(space_objects, menu)  # vis.py
        # задержка на 1/60 секунды
    #        time.sleep(1.0 / 60)
    # задержка до начала следующего фрейма

    print('Modelling finished!')
    pg.quit()


if __name__ == "__main__":
    main()
