import time

LOGS_PATH = "logging/logs"

def time_control(t, length_indicator=60, display='#'):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    cycle = 60 * t / length_indicator
    
    for _ in range(length_indicator):
        print(display, flush=True, end='')
        time.sleep(cycle)
    print()
    TEXT = f'Cycle of {t} minutes complete at {time.asctime()}'
    write_logs(LOGS_PATH, TEXT)


def write_logs(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
