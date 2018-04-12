import socket
import threading
import time
import command as cmd


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        result = cmd.getcmd(data)
        if result == "cann't find this command":
            sock.send("cann't find this command")
        else:
            sock.send(result)
        print(data)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            print(data)
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


class TransmitServer(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('0.0.0.0', port))
        self.s.listen(5)
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            self.sock, self.addr = self.s.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=tcplink, args=(self.sock, self.addr))
            t.start()


def main():
    TransmitServer("123", 8080)


if __name__ == '__main__':
    main()
