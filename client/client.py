# 导入socket库:
import socket


# 建立连接:
#s.connect(('www.sina.com.cn', 80))

class ConClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        # self.s=# 创建一个socket:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.ip, self.port))

    def recv(self):
        # 接收数据:
        buffer = []
        while True:
            # 每次最多接收1k字节:
            d = self.s.recv(10240)
            print(d)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)
        return data


def main():
    ConC = ConClient("139.199.213.83", 8080)
    ConC.connect()
    data = ConC.recv()
    print(data)


if __name__ == '__main__':
    main()
