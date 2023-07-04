import datetime as dt
import time
from colorama import Back
from playsound import playsound

LOGS_PATH = "logs"

def time_control(t, length_indicator=60, display=' '):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    cycle = 60 * t / length_indicator
    point_1 = length_indicator / 5
    point_2 = point_1 * 2
    point_3 = point_1 * 3
    point_4 = point_1 * 4
    start_time = dt.datetime.now()
    try:
        for i in range(length_indicator):
            if i <= point_1:
                print(Back.LIGHTGREEN_EX + display, flush=True, end='')
                time.sleep(cycle)
                
            elif point_1 < i <= point_2:
                print(Back.GREEN + display, flush=True, end='')
                time.sleep(cycle)
                
            elif point_2 < i <= point_3:
                print(Back.YELLOW + display, flush=True, end='')
                time.sleep(cycle)
                
            elif point_3 < i <= point_4:
                print(Back.MAGENTA + display, flush=True, end='')
                time.sleep(cycle)
                
            else:
                print(Back.RED + display, flush=True, end='')
                time.sleep(cycle)


    except KeyboardInterrupt:
        stop_time = dt.datetime.now()
        time_diff = stop_time - start_time
        time_diff_in_min = time_diff.seconds // 60
        print(Back.RESET + f'\nCycle interruption at {time_diff_in_min} minute')
        write_logs(LOGS_PATH, f'Cycle of {time_diff_in_min} minutes complete at {time.asctime()}. Interruption\n')
        return


    print(Back.RESET + f'\nCycle of {t} minutes finished. Take a rest!')
    playsound("finish_cycle.mp3")
    TEXT = f'Cycle of {t} minutes complete at {time.asctime()}\n'
    write_logs(LOGS_PATH, TEXT)
        

def write_logs(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
