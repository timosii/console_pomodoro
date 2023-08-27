## Description
The basic console timer for concentration work
## Install
1. First step
```
git clone https://github.com/timosii/console_pomodoro.git
cd console_pomodoro
```
2. Second step
```
make install
make build
make package-install
```
## Usage
- For work
```
pomodoro work <time in minutes>
```
- For rest
```
pomodoro rest <time in minutes>
```
At the end of the cycle, a signal will sound and logs will be recorded in the logs file.
Enjoy!
