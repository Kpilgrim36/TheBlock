from flask import *
import RPi.GPIO as GPIO
import time
import threading


app = Flask(__name__)

PIN = 18
PIN2 = 23
second = 2
i = False
temp = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)



@app.route("/red_led_on", methods=["POST"])
def red_led_on():
    print("Red LED on")
    GPIO.output(18, GPIO.HIGH)
    return "ok"


@app.route("/red_led_off", methods=["POST"])
def red_led_off():
    print("Red LED off")
    GPIO.output(18, GPIO.LOW)
    return "ok"


@app.route("/yellow_led_on", methods=["POST"])
def yellow_led_on():
    print("yellow LED on")
    GPIO.output(23, GPIO.HIGH)
    return "ok"


@app.route("/yellow_led_off", methods=["POST"])
def yellow_led_off():
    print("yellow LED off")
    GPIO.output(23, GPIO.LOW)
    return "ok"


@app.route("/blinking_thread", methods=["POST"])
def blinking_thread():
    global temp
    temp = True
    thread1 = threading.Thread(target=blink_on)
    thread1.start()
    return"Blinking On"


def blink_on():
    global temp
    print("blinking LED's on")
    while temp:
        print("Red on, Yellow off")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        time.sleep(.1)
        print("Yellow on, Red off")
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(.1)
        if not temp:
            break


@app.route("/blinking_off", methods=["POST"])
def blink_off():
    global temp
    temp = False
    thread2 = threading.Thread(target=blink_on)
    thread2.start()
    thread2.join(0)
    print("blinking LED's off in two seconds")
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    return "Blinking Off"


@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Kile Pilgrim")
