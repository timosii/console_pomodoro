from pomodoro.parser_args import take_args
from pomodoro.logic import time_control

def main():
    time, indicator_length, display = take_args()
    time_control(time, indicator_length, display)
    


if __name__ == '__main__':
    main()
