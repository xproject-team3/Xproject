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

src = "/home/pi/tt/"  # 저장되는 디렉터리

dte = time.localtime()
Year = dte.tm_year
Mon = dte.tm_mon
Day = dte.tm_mday
Hour = dte.tm_hour
Min = dte.tm_min
Sec = dte.tm_sec

time = str(Year) + "-" + str(Mon)+"-" + str(Day)+" "+str(Hour)+":"+str(Min)  # 메시지에 보낼 시간 정보
time2 = str(Year)+"_"+str(Mon)+"_"+str(Day)+"_"+str(Hour)+"_"+str(Min)  #파일명에 쓰일 시간



def echo_client(server_addr):
    i = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)
    print('connected: ', sock.getpeername())
    while True:
        #message = sys.stdin.readline()
        #if message == '\n':
            #distance=[]
        ser.write("in".encode('utf-8'))
        distance = float(ser.readline())
        print(distance)
        if distance < 5 :
            print('cam')
            with picamera.PiCamera() as camera:
                camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
                camera.capture('/home/pi/tt/%s.jpg' % time2)
                camera.stop_preview()
            capture_file_name = src + str(time2) + ".jpg" # 어떤 파일 형태로
            file = open(capture_file_name, "rb")
            data = file.read(8192)
            while(data):
                sock.send(data)
                data = file.read(8192)
            file.close()
            print("send finished")
                #distance=[]
	

    sock.close()

if __name__ == '__main__':
    echo_client(('192.168.0.63',50011))


