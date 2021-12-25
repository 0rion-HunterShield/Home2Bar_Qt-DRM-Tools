import base64
from io import StringIO
from cryptography.fernet import Fernet
import base64

class licensed:
    def run(self):
        data='''{code}'''

        key=bytes()
        with open('key.txt','rb') as xkey:
            key=xkey.read()

        f = Fernet(key)

        decoded = f.decrypt(data.encode())
        print(decoded)

        compiled=compile(source=decoded,filename='',mode='exec')
        exec(decoded,globals())

    program=''''''


x=licensed()
x.run()
