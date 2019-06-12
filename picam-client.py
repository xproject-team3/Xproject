import socket
import serial
import time
import picamera

port = "/dev/ttyACM0"  #아두이노의 포트
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
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)
    print('connected: ', sock.getpeername())
    while True:

        ser.write("in".encode('utf-8'))
        distance = float(ser.readline())
        print(distance)
        if distance < 20 and distance >4:
            print('cam')  # 사진 촬영시 cam 이라고 print
            with picamera.PiCamera() as camera: #context관리를 자동으로 해주는 with 사용
                camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
                camera.capture('/home/pi/tt/%s.jpg' % time2) # 라즈베리파이의 tt폴더에 저장
                camera.stop_preview()
            capture_file_name = src + str(time2) + ".jpg" # 어떤 파일 형태로
            file = open(capture_file_name, "rb")  # 전달할 사진을 바이너리 형식으로 읽음
            data = file.read(8192)  #1KB를 읽음
            while(data):
                sock.send(data) # 데이터 전송
                data = file.read(8192) #1KB씩 읽음
            print("send finished")  # 서버에 전송 되었을때 send finished 라고 전송
            
	

    sock.close()

if __name__ == '__main__':
    echo_client(('192.168.0.63',50011))





