import socket
import sys
import time
import errno
from multiprocessing import Process
import math

init_message = ('Welcome to the Calculator\n\n1. Logarithm\n2. Square Root\n3. Exponential\n4. Power\n5. Exit\nEnter number which mathematical function to choose from')

def loga():
    s_sock.send(str.encode('Enter number to log'))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    s_sock.send(str.encode('Enter base of log'))
    base = s_sock.recv(2048)
    base = base.decode('utf-8')
    base = int(base)
    print(f'base is {base}')
    ans = math.log(x, base)
    print(f'Answer is {ans}')
    s_sock.sendall(str.encode(f'Answer: {ans}'))

def squa():
    s_sock.send(str.encode('Enter number to square root'))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    ans = math.sqrt(x)
    print(f'Answer is {ans}')
    s_sock.sendall(str.encode(f'Answer: {ans}'))

def expo():
    s_sock.send(str.encode('Enter power for exponent'))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    ans = math.exp(x)
    print(f'Answer is {ans}')
    s_sock.sendall(str.encode(f'Answer: {ans}'))

def power():
    s_sock.send(str.encode('Enter number to power'))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    s_sock.send(str.encode('Enter power'))
    powe = s_sock.recv(2048)
    powe = powe.decode('utf-8')
    powe = int(powe)
    print(f'power is {powe}')
    ans = math.pow(x, powe)
    print(f'Answer is {ans}')
    s_sock.sendall(str.encode(f'Answer: {ans}'))

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Calculator\n\n1. Logarithm\n2. Square Root\n3. Exponential\n4. Power\n5. Exit\nEnter number which mathematical function to choose from'))
    while True:
        enc_data = s_sock.recv(2048)
        data = enc_data.decode('utf-8')
        print(data)
        if not data:
            break
        if data == '1':
            loga()
        elif data == '2':
            squa()
        elif data == '3':
            expo()
        elif data == '4':
            power()
        elif data == '5':
            break
        else:
            continue
        s_sock.sendall(str.encode(init_message))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                print('Connected')
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:
                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
       	sys.exit(1)
    finally:
     	   s.close()

