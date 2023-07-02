import argparse

def take_args():
    parser = argparse.ArgumentParser(description="Use your console for time managment")
    parser.add_argument('time_in_minutes', type=int, help='duration of one cycle')
    parser.add_argument('indicator_lenght', type=int, \
                        help='the length of the strip of one cycle (in chars)')
    parser.add_argument('-d', '--display', help='choose your indicator', default='#')
    args = parser.parse_args()
    time = args.time_in_minutes
    indicator = args.indicator_lenght
    display = args.display
    return time, indicator, display



