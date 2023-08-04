import serial
import csv
import datetime

port = "/dev/ttyACM0"  # serial port of Arduino
baudrate = 9600  # arduino uno runs at 9600 baud
now = datetime.datetime.now() # full time
fileName = "SSIRealVoltage" + str(datetime.date.today()) +"--" + str(datetime.datetime.time(now).hour) + \
           "_" + str(datetime.datetime.time(now).minute) +".csv"  # name of the CSV file generated (I'm sure there's an easier way to do this :/)
print("Connected to Arduino port:" + port)
file = open(fileName, "w")
print("Created file")
# headerList = ['date/time', 'distance measured', 'mimicked voltage']

ser = serial.Serial(port, 9600)
sensor_data = []  # store data
while True:
    getData = ser.readline()
    dataString = getData.decode('utf-8')
    data = dataString[0:][:-2]

    now = datetime.datetime.now()
    date = datetime.date.today()
    time = datetime.datetime.time(now)
    # data = str(now) + ", " + data
    data = data + ", " + str(date) + ", " + str(time) + ", " + str(now)
    readings = data.split(", ")
    print(readings)

    sensor_data.append(readings)
    # print(sensor_data)
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)

    file.close()
