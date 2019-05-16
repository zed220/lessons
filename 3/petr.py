import time
import playsound

seconds = input("Сколько секунд считать:")
seconds = int(seconds)
for x in range(seconds,0,-1):
    print(x)
    time.sleep(1)
playsound.playsound("beep.mp3")