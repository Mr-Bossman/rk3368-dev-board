from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
data_file = open("pins.txt", "r")
pins = dict()
invis = False

def press_and_release(key):
	time.sleep(.1)
	keyboard.press(key)
	time.sleep(.1)
	keyboard.release(key)
	time.sleep(.1)

def SetInvis(inv):
	if inv != invis:
		for _ in range(0, 6):
			press_and_release(Key.tab)
		press_and_release(Key.space)

def makePin(pinName, pinNumber):
	press_and_release(Key.enter)
	print(pinNumber + " ," + pinName )
	keyboard.type(pinName)
	press_and_release(Key.tab)
	keyboard.type(pinNumber)
	SetInvis(False)
	press_and_release(Key.enter)
	press_and_release(Key.down)
	press_and_release(Key.down)
	press_and_release(Key.enter)


def makePinInvis(pinName, pinNumber):
	press_and_release(Key.enter)
	print(pinNumber + " ," + pinName )
	keyboard.type(pinName)
	press_and_release(Key.tab)
	keyboard.type(pinNumber)
	SetInvis(True)
	press_and_release(Key.enter)
	press_and_release(Key.enter)



time.sleep(5)
for aline in data_file:
	val = aline.split()
	if val[1] in pins:
		pins[val[1]] = pins[val[1]] + (val[0],)
	else:
		pins.update({val[1]:(val[0], )})

for tuples in pins:
	for pin in pins[tuples]:
		if pin == pins[tuples][0]:
			makePin(str(tuples),str(pin))
			invis = False
		else:
			makePinInvis(str(tuples),str(pin))
			invis = True


