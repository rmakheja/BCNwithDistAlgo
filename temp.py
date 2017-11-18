import signal
def timeout_handler(signal, frame):
    # print("I donno where I am")
    fh = open("112hello.txt", "w")
    fh.write("Hello World. Time is up.")
    fh.close()
    raise Exception("end of time")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(1)

try:
    lives = 10
    while lives > 0:
        print('Main thread stuff')
except Exception as e:
    # print(exc)
    print("In exception - " + str(e))
    # signal.alarm(0)