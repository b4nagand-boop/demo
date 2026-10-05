import time

incr = 1
state = 0
max_indent = 20

while True:
    print(" " * state + "Hello!")
    state += incr

    if state == max_indent or state == 0:
        incr = -incr

    time.sleep(0.05)