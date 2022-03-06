import time
from adafruit_motorkit import MotorKit
import keyboard

kit = MotorKit()

print ("Inicializado...Ctrl para sair")

anterior = None

while True:
	key = keyboard.read_key()
	if (key == 'w'):
		kit.motor1.throttle = 0.5
		kit.motor2.throttle = 0.5
		anterior = 'w'
		while True:
			if (not (keyboard.is_pressed('w'))):
				break
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
	elif (key == 's'):
		kit.motor1.throttle = -0.5
		kit.motor2.throttle = -0.5
		anterior = 's'
		while True:
			if (not (keyboard.is_pressed('s'))):
				break
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
	elif (key == 'a'):
		if (anterior == 'w'):
			kit.motor1.throttle = 0.1
			kit.motor2.throttle = 0.4
		elif (anterior == 's'):
			kit.motor1.throttle = -0.1
			kit.motor2.throttle = -0.4
		while True:
			if (not (keyboard.is_pressed('a'))):
				break
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
	elif (key == 'd'):
		if (anterior == 'w'):
			kit.motor1.throttle = 0.4
			kit.motor2.throttle = 0.1
		elif (anterior == 's'):
			kit.motor1.throttle = -0.4
			kit.motor2.throttle = -0.1
		while True:
			if (not (keyboard.is_pressed('d'))):
				break
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
	elif (key == 'space'):
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
		while True:
			if (not (keyboard.is_pressed('space'))):
				break
	elif (key == 'ctrl'):
		kit.motor1.throttle = 0
		kit.motor2.throttle = 0
		while True:
			if (not (keyboard.is_pressed('ctrl'))):
				break
		print ("Encerrando...")
		break
	else:
		pass

