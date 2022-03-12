from machine import Pin
import utime

rows = []
print("--- STARTED ---") # log

status_led = Pin(25, Pin.OUT)
status_led.value(1) # turn the litle green led on the pico board on

rows.append(Pin(1, Pin.OUT))  # row1
rows.append(Pin(2, Pin.OUT))  # row2
rows.append(Pin(3, Pin.OUT))  # row3
rows.append(Pin(4, Pin.OUT))  # row4
rows.append(Pin(5, Pin.OUT))  # row5

for _ in range(12):
    for row in rows:
        row.toggle() # toggle row
        utime.sleep(0.2) # sleep for 0.2sec
    print(str(_ + 1) + " : Finished") # log

for row in rows:
    row.value(0) # turn everything off incase its still on
status_led.value(0) # turn the little green led off
print("--- FINISHED ---") # log
