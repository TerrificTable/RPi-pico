from machine import Pin
import utime

rows = []

print("--- STARTED ---")

status_led = Pin(25, Pin.OUT)
status_led.value(1)

rows.append(Pin(1, Pin.OUT))  # line1
rows.append(Pin(2, Pin.OUT))  # line2
rows.append(Pin(3, Pin.OUT))  # line3
rows.append(Pin(4, Pin.OUT))  # line4
rows.append(Pin(5, Pin.OUT))  # line5

for _ in range(12):
    for row in rows:
        row.toggle()
        utime.sleep(0.2)
    print(str(_ + 1) + " : Finished")

for row in rows:
    row.value(0)
status_led.value(0)
print("--- FINISHED ---")
