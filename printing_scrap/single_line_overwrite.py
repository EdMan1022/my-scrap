import sys
import time

for i in range(10):
    print("Loading{}".format(i * "."))
    sys.stdout.write("\033[F")
    time.sleep(.5)
    sys.stdout.write("\033[K")
