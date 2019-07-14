import RPi.GPIO as GPIO
import time

PIN = 13
SIG1 = "1011011001001011001001001001001001011"

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(PIN, GPIO.OUT)
   GPIO.output(PIN, GPIO.LOW)

def send(msg):
  for i in range(10):
    for s in msg:
#       print(s)
       if s=="0":
          GPIO.output(PIN, GPIO.LOW)
       elif s=="1":
          GPIO.output(PIN, GPIO.HIGH)
       time.sleep(0.000300)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.011000)

def main():
   print('debut')
   setup()
   CMD=1
   while (1):
      if (CMD == 1):
         send(SIG1)
         CMD=0
      elif (CMD==0):
          time.sleep(1)
      else:
         print('signal inconnu')

main()

