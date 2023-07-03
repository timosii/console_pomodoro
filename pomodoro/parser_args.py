import argparse

def take_args():
    parser = argparse.ArgumentParser(description="Use your console for time managment")
    parser.add_argument('time_in_minutes', type=int, help='duration of one cycle')
    parser.add_argument('-l', '--lenght_indicator', type=int, help='the length \
    of the strip of one cycle (in chars)', default=60)
    parser.add_argument('-d', '--display', \
                        help='choose char for indication', default=' ')
    args = parser.parse_args()
    time = args.time_in_minutes
    indicator = args.lenght_indicator
    display = args.display
    return time, indicator, display



