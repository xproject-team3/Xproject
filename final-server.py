from socket import socket,AF_INET, SOCK_STREAM # 소켓 임포트
import time


#이미지 파일 저장 위치
src = "C:/Users/cheal/AndroidStudioProjects/xproject/app/src/main/res/drawable/"

# a를 넣고 부르면 이미지파일 저장 b를 넣고 부르면 text 파일에 저장
def fileName(x):
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec

    textFile = str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min)
    imgFileName = src + textFile + '.jpg'

    if x == 'a':
        return imgFileName
    elif x=='b':
        return textFile

def echo_server(my_port):
    sock = socket(AF_INET, SOCK_STREAM)  # 소켓 객체를 생성
    sock.bind(('192.168.0.63', my_port)) # 소켓객체에 주소값을 바인딩 시킴 호스트와 포트로 된 튜플값을 인자로 받음
    sock.listen(5)   # 리스닝 수 = 5
    print('server started')
    while True:   # 프로세스가 죽을때 까지
        conn, client_addr = sock.accept()  # 서버소켓에 클라이언트가 연결되면 클라이언트 소켓, 주소를 반환
        print('connected by', client_addr)  # 어떤 주소에서 연결되었는지 프린트
        try:
            f = open(fileName('a') , 'wb')  #시간정보를 받아와서 파일을 write binary로 open

            while True:
                data = conn.recv(4096)  #데이터를 512Byte씩 받아와서
                if not data:  # 데이터가 오지 않을때 까지
                    break
                else:
                    f.write(data) # 파일을 작성
            f.close()
            file = open(src + 'filename.txt', 'a') # 텍스트파일(LOG) 에
            file.write(fileName('b') + '\n') # 현재 시간을 저장
            file.close()

#'''    # wb모드로 open한 이유
        # 바이너리 파일에는 파일의 형식에 관한 내용이 포함되기 때문에
        # 바이너리 파일을 전송하면 파일 형식에 대한 언급 없이도 자동으로 JPG ,txt 파일을 만들 수 있다.
        # 또한 소켓은 bytes 를 전달하기 때문에 별다른 디코딩 과정없이 파일에 작성해도 된다.'''#



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


