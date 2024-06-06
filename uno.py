import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

# val = input("select Port: COM")
val = 3
for x in range(0, len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
# print("first check")

command = "ENTER"
print("1st check")
serialInst.write(command.encode("utf-8"))
# print("2nd check")
# command = input("arduinoCmd TYPE ENTER:  ")
# command = "ENTER"
# exit()
while True:
    ex1it = input("Type: exit:  ")
    print("3rd  check")
    if ex1it == "exit":
        exit()
