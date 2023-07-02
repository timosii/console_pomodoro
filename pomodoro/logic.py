import time


def time_control(t, indicator_length, display='#'):
    '''
    На вход поступает необходимое время в минутах.
    Возвращает None, заканчивает работу, спустя это время
    '''
    time_sec = 60 * t
    cycle = time_sec // indicator_length
    for _ in range(indicator_length):
        print(display, flush=True, end=' ')
        time.sleep(cycle)

        
