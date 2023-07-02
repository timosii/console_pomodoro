import time

LOGS_PATH = "logging/logs"


def time_control(t, indicator_length=60, display='#'):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    time_sec = 60 * t
    cycle = time_sec / indicator_length
    
    for _ in range(indicator_length):
        print(display, flush=True, end='')
        time.sleep(cycle)

    print()
    TEXT = f'Cycle of {t} minutes complete at {time.asctime()}'
    write_logs(LOGS_PATH, TEXT)


def write_logs(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
