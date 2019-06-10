from socket import socket,AF_INET, SOCK_STREAM # 소켓 임포트
import sqlite3
import os
import time
import sys


#이미지 파일 저장 위치
src = "C:/Users/cheal/AndroidStudioProjects/xproject/app/src/main/res/drawable/"


def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src +'d'+ str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min) +'.jpg'
    return imgFileName

def echo_server(my_port):
    sock = socket(AF_INET, SOCK_STREAM)  # 소켓 객체를 생성
    sock.bind(('192.168.0.63', my_port)) # 소켓객체에 주소값을 바인딩 시킴 호스트와 포트로 된 튜플값을 인자로 받음
    sock.listen(5)   # 리스닝 수 = 5
    print('server started')
    while True:   # 프로세스가 죽을때 까지
        conn, client_addr = sock.accept()  # 서버소켓에 클라이언트가 연결되면 클라이언트 소켓, 주소를 반환
        print('connected by', client_addr)  # 어떤 주소에서 연결되었는지 프린트
        try:
            f = open(fileName(), 'wb')

            while True:
                data = conn.recv(4096)
                if not data:
                    break
                else:
                    f.write(data)
            f.close()
            file = open(src + 'fileName.txt', 'a')
            file.write(time.ctime() + '\n')
            file.close()







        # Exception Handling
        except OSError as e:
            print('socket error: ', e)
        except Exception as e:
            print('Exception at listening:'.format(e))
        else:
            print('client closed', client_addr)
        finally:
            conn.close()

if __name__ == '__main__':
    echo_server(50011)   # 포트번호
