import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    arduinoCommand = input("Serial Command: ON=on OFF=off")

    if arduinoCommand == "on":
        command.write("command".encode("utf-8"))
        print("ON")

    elif arduinoCommand == "off":
        command.write("exit".encode("utf-8"))
        print("OFF")

    if command.read() == "exit":
        exit()
