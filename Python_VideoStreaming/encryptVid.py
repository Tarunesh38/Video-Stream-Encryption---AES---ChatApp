import cv2
import socket
import threading
#import aes
import pickle
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
import numpy as np

# Encryption function
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    enc_data = cipher.encrypt(pad(data, AES.block_size))
    return enc_data

# Decryption function
def decrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    dec_data = unpad(cipher.decrypt(data), AES.block_size)
    return dec_data

class Transmitter(threading.Thread):
    def __init__(self,ip,port,key):
        threading.Thread.__init__(self) 
        self.ip = ip
        self.port = port
        self.key = key
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.cam = cv2.VideoCapture(0)

    def run(self):
        while(True):
            try:
                self.ret , self.frame = self.cam.read()
                self.frame = cv2.resize(self.frame,(640,480))
                self.data = pickle.dumps(self.frame)
                self.data = encrypt_data(self.data,self.key)
                self.sock.send(self.data + b'END!')
                try:
                    cv2.imshow('Transmitting',self.frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print(" -> Stopped Sending ! \n Exiting")
                        break
                except:
                    pass
            except Exception as e:
                print(e)
                print(" -> Broken Pipe ! \n Exiting")
                break
    
    def __del__(self):
        self.sock.close()
        self.cam.release()
        cv2.destroyAllWindows()

class Reciever(threading.Thread):
    def __init__(self,ip,port,key):
        threading.Thread.__init__(self)
        self.ip   = ip 
        self.port = port
        self.key = key
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((ip,port))
        print("Listening on {}:{}".format(ip,port))
        self.sock.listen(1)

    def run(self):
        self.conn , self.addr = self.sock.accept()
        print("Incoming Connection From{}".format(self.addr))
        t = b''
        while(True):
            data = b''
            while True:
                r = self.conn.recv(921776)
                if len(r)==0:
                    exit(0)
                end = r.find(b'END!')
                if end != -1:
                    data = t + data + r[:end]
                    t = r[end+4:]
                    break
                data += r

            if data is not None:
                try:
                    data = decrypt_data(data,self.key)
                    self.frame = pickle.loads(data)
                    cv2.imshow('Recieving',self.frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                except Exception as e:
                    print(e)
                    print(" -> Broken Pipe ! \n Exiting")
                    break
    
    def __del__(self):
        self.conn.close()
        self.sock.close()
        cv2.destroyAllWindows()