data_file = open("rk3368.txt", "r")
lib_file = open("test.lib", "w")
pins = dict()
lib_file.write('EESchema-LIBRARY Version 2.4\nDEF rk3368 U 0 40 Y Y 1 F N\nF0 "U" 0 0 50 H V C CNN\nF1 "rk3368" 0 0 50 H V C CNN\nF2 "" 0 0 50 H I C CNN\nF3 "" 0 0 50 H I C CNN\nDRAW\n')
for aline in data_file:
	
	val = aline.split()
	if val[1] in pins:
		pins[val[1]] = pins[val[1]] + (val[0],)
	else:
		pins.update({val[1]:(val[0], )})
pos = 0
for tuples in sorted(pins):
	for pin in pins[tuples]:
		if pin == pins[tuples][0]:
			lib_file.write("X " + str(tuples) + " " + str(pin) +" 0 " + str(pos) + " 100 L 50 50 1 1 I\n")

		else:
			lib_file.write("X " + str(tuples) + " " + str(pin) +" 0 " + str(pos) + " 100 L 50 50 1 1 I N\n")
	pos += 100
			
lib_file.write('ENDDRAW\nENDDEF')




