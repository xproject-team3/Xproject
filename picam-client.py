import sys , socket
import serial
import datetime
import os
import time
import picamera
import shutil

port = "/dev/ttyACM0"
ser = serial.Serial(port,9600)
ser.flushInput()

src = "/home/pi/tt/";  

dte = time.localtime()
Year = dte.tm_year
Mon = dte.tm_mon
Day = dte.tm_mday
Hour = dte.tm_hour
Min = dte.tm_min
Sec = dte.tm_sec

time = str(Year) + "-" + str(Mon)+"-" + str(Day)+" "+str(Hour)+":"+str(Min)
time2 = str(Year)+"_"+str(Mon)+"_"+str(Day)+"_"+str(Hour)+"_"+str(Min)

def transfer(filename):
    capture_file_name = src + str(filename) + ".jpg"
    file = open(capture_file_name, "rb")
    img_size = os.path.getsize(capture_file_name)
    img = file.read(img_size)
    file.close()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.0.138", 50011))

    client_socket.sendall(img)

    client_socket.close()
    print("Finish Send")


def echo_client(server_addr):
    i = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)
    print('connected: ', sock.getpeername())
    while True:
        message = sys.stdin.readline()
        if message == '\n':
            distance=[]  
            ser.write("in".encode('utf-8'))
            distance.append(float(ser.readline()))
            s_msg = "type:load\r\ntime:%s\r\ndistance %s\r\n" %(time,distance[0])  
            sock.send(s_msg.encode('utf-8'))
            if distance[0]<5 :
                print('cam')
                with picamera.PiCamera() as camera:
                    camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
                    camera.capture('/home/pi/tt/%s.jpg' % time2)
                    camera.stop_preview()
                transfer(time2)
                

	
        data = sock.recv(1024).decode('utf-8')
        #print(data,end='')
    sock.close()

if __name__ == '__main__':
    echo_client(('192.168.0.63',50011))
