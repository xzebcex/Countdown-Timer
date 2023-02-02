# Countdown.

import time

# Set the number of seconds for the Stopwatch or Countdown timer.
seconds = 10

# Stopwatch or Countdown timer.
while seconds > 0:
    print(seconds)
    time.sleep(1)  # delay of  1 second.
    seconds -= 1

print("You ran out of time")

