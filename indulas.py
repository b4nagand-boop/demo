import time
print("Hello world!")
incr = 1
state = 0
while True:
	print(state*" " + "Hello!")
	state += incr
	if state == 50 or state == -50:
		incr = incr * -1
		state = 0
	time.sleep(0.2)