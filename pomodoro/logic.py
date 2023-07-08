import datetime as dt
import time
from playsound import playsound
from rich.progress import track

LOGS_PATH = "logs"

def time_control(t):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    start_time = dt.datetime.now()
    try:
        for _ in track(range(100), description='[green]Keep working ...'):
            time_cycle(60 * t/100)


    except KeyboardInterrupt:
        stop_time = dt.datetime.now()
        time_diff = stop_time - start_time
        time_diff_in_min = time_diff.seconds // 60
        print(f'\nCycle interruption at {time_diff_in_min} minute')
        if time_diff_in_min >= 5:
            write_logs(LOGS_PATH, f'Cycle of {time_diff_in_min} minutes complete at {time.asctime()}. Interruption\n')
        return


    print(f'\nCycle of {t} minutes finished. Take a rest!')
    playsound("finish_cycle.mp3")
    TEXT = f'Cycle of {t} minutes complete at {time.asctime()}\n'
    if t >= 5:
        write_logs(LOGS_PATH, TEXT)
 

def time_cycle(cycle):
    time.sleep(cycle)


def write_logs(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
