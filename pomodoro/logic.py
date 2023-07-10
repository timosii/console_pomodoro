import datetime as dt
import time
from playsound import playsound
from rich.progress import track

LOGS_PATH = "logs"

def time_control(activity, t):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    start_time = dt.datetime.now()
    if activity == 'work':
        entry_message = '[green]Keep working ...'
        finish_message = 'Take a rest!'
    elif activity == 'rest':
        entry_message = '[green]Keep resting ...'
        finish_message = "Let's go to work!"
    else:
        print('Choose your activity - work or rest')
        return
    try:
        for _ in track(range(100), description=entry_message):
            time_cycle(60 * t/100)


    except KeyboardInterrupt:
        stop_time = dt.datetime.now()
        time_diff = stop_time - start_time
        time_diff_in_min = time_diff.seconds // 60
        print(f'\nCycle of {activity} has been interrupted at {time_diff_in_min} minute')
        if time_diff_in_min >= 5:
            write_logs(LOGS_PATH, f'The {time_diff_in_min} minute {activity} cycle was interrupt at {time.asctime()}\n')
        return


    print(f'\nThe {t} minute {activity} cycle finished. {finish_message}')
    playsound("finish_cycle.mp3")
    TEXT = f'{t} minute {activity} cycle was complete at {time.asctime()}\n'
    if t >= 5:
        write_logs(LOGS_PATH, TEXT)


def time_cycle(cycle):
    time.sleep(cycle)


def write_logs(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
