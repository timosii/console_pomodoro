import argparse

def take_args():
    parser = argparse.ArgumentParser(description="Use your console for time managment")
    parser.add_argument('activity', help='choose type of activity: work or rest')
    parser.add_argument('time_in_minutes', type=int, help='duration of one cycle')
    args = parser.parse_args()
    activity = args.activity
    time = args.time_in_minutes
    return activity, time



