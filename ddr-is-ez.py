#knowing coding makes ur life ez
data_file = open("ddr3-sodim", "r")



pins = [str()]
for aline in data_file:
	
	val = aline.split()
	pins.insert(int(val[0]), val[1])

pos = 0


for pin in range(1,len(pins),2):
	print("Text Label " + str((int((pin-1)/2)+1)*100) + " 900  1    50   ~ 0\n" + pins[pin] )
for pin in range(2,len(pins),2):
	print("Text Label " + str((int((pin)/2)+102)*100) + " 900  1    50   ~ 0\n" + pins[pin])

pins.sort()
print("\n\n\n\n\n\n\n\n\n\n\n\n")
for pin in range(1,len(pins)):
	print("Text Label " + str(pin*100) + " 100  1    50   ~ 0\n" + pins[pin] )

