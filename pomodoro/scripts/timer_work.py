from pomodoro.parser_args import take_args
from pomodoro.logic import time_control

def main():
    activity, time = take_args()
    time_control(activity, time)    


if __name__ == '__main__':
    main()
