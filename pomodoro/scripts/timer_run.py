from pomodoro.parser_args import take_args
from pomodoro.logic import time_control

def main():
    time, length_indicator, display = take_args()
    time_control(time, length_indicator, display)
    


if __name__ == '__main__':
    main()
