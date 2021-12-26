#! /usr/bin/env python3
from cryptography.fernet import Fernet
import base64


def encrypt():
    data=''''''
    with open('Home2Bar_Qt.py','rb') as x:
        data=x.read()



    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(data)
    return token,key
def writeTO():
    result=encrypt()
    with open('tkn.txt','wb') as out1,open('key.txt','wb') as out2:
        out1.write(result[0])
        out2.write(result[1])

with open('licensed_template.py','r') as f,open('key.txt','wb') as key,open('licensed.py','w') as tkn:
    code=f.read()
    result=encrypt()
    z=code.format(code=result[0].decode('utf-8'))
    tkn.write(z)
    key.write(result[1])
