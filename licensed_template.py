import base64
from io import StringIO
from cryptography.fernet import Fernet
import base64
import shutil,csv,string,requests,time,sys,os,pyqrcode,base64,json,cairosvg
from io import BytesIO,StringIO
from pathlib import Path
from copy import deepcopy as copy
import platform
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot,pyqtSignal
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView

class Loader(QMainWindow,QWidget):
    ui='''PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHVpIHZlcnNpb249IjQuMCI+
CiA8Y2xhc3M+TG9hZGVyTm9LZXlGaWxlPC9jbGFzcz4KIDx3aWRnZXQgY2xhc3M9IlFNYWluV2lu
ZG93IiBuYW1lPSJMb2FkZXJOb0tleUZpbGUiPgogIDxwcm9wZXJ0eSBuYW1lPSJnZW9tZXRyeSI+
CiAgIDxyZWN0PgogICAgPHg+MDwveD4KICAgIDx5PjA8L3k+CiAgICA8d2lkdGg+NDI0PC93aWR0
aD4KICAgIDxoZWlnaHQ+MTgyPC9oZWlnaHQ+CiAgIDwvcmVjdD4KICA8L3Byb3BlcnR5PgogIDxw
cm9wZXJ0eSBuYW1lPSJ3aW5kb3dUaXRsZSI+CiAgIDxzdHJpbmc+TG9hZGVyTm9LZXlGaWxlPC9z
dHJpbmc+CiAgPC9wcm9wZXJ0eT4KICA8d2lkZ2V0IGNsYXNzPSJRV2lkZ2V0IiBuYW1lPSJjZW50
cmFsd2lkZ2V0Ij4KICAgPGxheW91dCBjbGFzcz0iUUdyaWRMYXlvdXQiIG5hbWU9ImdyaWRMYXlv
dXQiPgogICAgPGl0ZW0gcm93PSIwIiBjb2x1bW49IjAiIGNvbHNwYW49IjIiPgogICAgIDx3aWRn
ZXQgY2xhc3M9IlFMYWJlbCIgbmFtZT0ibGFiZWwiPgogICAgICA8cHJvcGVydHkgbmFtZT0idGV4
dCI+CiAgICAgICA8c3RyaW5nPk5vICdrZXkgZmlsZSAoa2V5LnR4dCknIHdhcyBmb3VuZCEgVHJ5
IGVudGVyaW5nIHRoZSBrZXkgbWFudWFsbHk/PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAg
ICAgPC93aWRnZXQ+CiAgICA8L2l0ZW0+CiAgICA8aXRlbSByb3c9IjEiIGNvbHVtbj0iMCI+CiAg
ICAgPHdpZGdldCBjbGFzcz0iUUxpbmVFZGl0IiBuYW1lPSJrZXlfZGF0YSI+CiAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJ0b29sVGlwIj4KICAgICAgIDxzdHJpbmc+a2V5IGRhdGEgdG8gYmUgZW50ZXJl
ZDwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVz
VGlwIj4KICAgICAgIDxzdHJpbmc+a2V5IGRhdGEgdG8gYmUgZW50ZXJlZDwvc3RyaW5nPgogICAg
ICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgIDxz
dHJpbmc+a2V5IGRhdGEgdG8gYmUgZW50ZXJlZDwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5Pgog
ICAgICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgPHN0cmluZz5rZXkg
ZGF0YSB0byBiZSBlbnRlcmVkPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9w
ZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgPHN0cmluZz5rZXkgZGF0
YSB0byBiZSBlbnRlcmVkPC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0
eSBuYW1lPSJkcmFnRW5hYmxlZCI+CiAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAgICA8L3By
b3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0icGxhY2Vob2xkZXJUZXh0Ij4KICAgICAgIDxz
dHJpbmc+S2V5IERhdGE8L3N0cmluZz4KICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3BlcnR5
IG5hbWU9ImNsZWFyQnV0dG9uRW5hYmxlZCI+CiAgICAgICA8Ym9vbD50cnVlPC9ib29sPgogICAg
ICA8L3Byb3BlcnR5PgogICAgIDwvd2lkZ2V0PgogICAgPC9pdGVtPgogICAgPGl0ZW0gcm93PSIx
IiBjb2x1bW49IjEiPgogICAgIDx3aWRnZXQgY2xhc3M9IlFQdXNoQnV0dG9uIiBuYW1lPSJzdWJt
aXRfa2V5Ij4KICAgICAgPHByb3BlcnR5IG5hbWU9InRvb2xUaXAiPgogICAgICAgPHN0cmluZz5z
dWJtaXQga2V5PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1l
PSJzdGF0dXNUaXAiPgogICAgICAgPHN0cmluZz5zdWJtaXQga2V5PC9zdHJpbmc+CiAgICAgIDwv
cHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ3aGF0c1RoaXMiPgogICAgICAgPHN0cmlu
Zz5zdWJtaXQga2V5PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxwcm9wZXJ0eSBu
YW1lPSJhY2Nlc3NpYmxlTmFtZSI+CiAgICAgICA8c3RyaW5nPnN1Ym1pdCBrZXk8L3N0cmluZz4K
ICAgICAgPC9wcm9wZXJ0eT4KICAgICAgPHByb3BlcnR5IG5hbWU9ImFjY2Vzc2libGVEZXNjcmlw
dGlvbiI+CiAgICAgICA8c3RyaW5nPnN1Ym1pdCBrZXk8L3N0cmluZz4KICAgICAgPC9wcm9wZXJ0
eT4KICAgICAgPHByb3BlcnR5IG5hbWU9InRleHQiPgogICAgICAgPHN0cmluZz5TdWJtaXQ8L3N0
cmluZz4KICAgICAgPC9wcm9wZXJ0eT4KICAgICA8L3dpZGdldD4KICAgIDwvaXRlbT4KICAgIDxp
dGVtIHJvdz0iMiIgY29sdW1uPSIwIiBjb2xzcGFuPSIyIj4KICAgICA8d2lkZ2V0IGNsYXNzPSJR
UHVzaEJ1dHRvbiIgbmFtZT0icXVpdCI+CiAgICAgIDxwcm9wZXJ0eSBuYW1lPSJ0b29sVGlwIj4K
ICAgICAgIDxzdHJpbmc+cXVpdCBhcyB5b3UgZG9uJ3QgaGF2ZSBhIGtleTwvc3RyaW5nPgogICAg
ICA8L3Byb3BlcnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0ic3RhdHVzVGlwIj4KICAgICAgIDxz
dHJpbmc+cXVpdCBhcyB5b3UgZG9uJ3QgaGF2ZSBhIGtleTwvc3RyaW5nPgogICAgICA8L3Byb3Bl
cnR5PgogICAgICA8cHJvcGVydHkgbmFtZT0id2hhdHNUaGlzIj4KICAgICAgIDxzdHJpbmc+cXVp
dCBhcyB5b3UgZG9uJ3QgaGF2ZSBhIGtleTwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5PgogICAg
ICA8cHJvcGVydHkgbmFtZT0iYWNjZXNzaWJsZU5hbWUiPgogICAgICAgPHN0cmluZz5xdWl0IGFz
IHlvdSBkb24ndCBoYXZlIGEga2V5PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAgIDxw
cm9wZXJ0eSBuYW1lPSJhY2Nlc3NpYmxlRGVzY3JpcHRpb24iPgogICAgICAgPHN0cmluZz5xdWl0
IGFzIHlvdSBkb24ndCBoYXZlIGEga2V5PC9zdHJpbmc+CiAgICAgIDwvcHJvcGVydHk+CiAgICAg
IDxwcm9wZXJ0eSBuYW1lPSJ0ZXh0Ij4KICAgICAgIDxzdHJpbmc+UXVpdCEgSSBkb24ndCBoYXZl
IGEga2V5Ljwvc3RyaW5nPgogICAgICA8L3Byb3BlcnR5PgogICAgIDwvd2lkZ2V0PgogICAgPC9p
dGVtPgogICA8L2xheW91dD4KICA8L3dpZGdldD4KICA8d2lkZ2V0IGNsYXNzPSJRTWVudUJhciIg
bmFtZT0ibWVudWJhciI+CiAgIDxwcm9wZXJ0eSBuYW1lPSJnZW9tZXRyeSI+CiAgICA8cmVjdD4K
ICAgICA8eD4wPC94PgogICAgIDx5PjA8L3k+CiAgICAgPHdpZHRoPjQyNDwvd2lkdGg+CiAgICAg
PGhlaWdodD4zMjwvaGVpZ2h0PgogICAgPC9yZWN0PgogICA8L3Byb3BlcnR5PgogIDwvd2lkZ2V0
PgogIDx3aWRnZXQgY2xhc3M9IlFTdGF0dXNCYXIiIG5hbWU9InN0YXR1c2JhciIvPgogPC93aWRn
ZXQ+CiA8cmVzb3VyY2VzLz4KIDxjb25uZWN0aW9ucy8+CjwvdWk+Cg=='''
    def submit_key(self):
        print('submitting key...',self.window.key_data.text())
        with open(self.keyfile,'wb') as out:
            out.write(self.window.key_data.text().encode())
        self.window.close()
    quitting=False

    def quitting_f(self):
        self.quitting=True
        self.window.close()

    def setup_buttons(self):
        self.window.submit_key.clicked.connect(self.submit_key)
        self.window.quit.clicked.connect(self.quitting_f)
    
    def __init__(self,parent=None,keyfile=None):
        self.keyfile=keyfile
        if os.geteuid() == 0:
            self.window=uic.loadUi("main.ui")
            exit("you should not be root!")
        self.app=QApplication(sys.argv)
        super().__init__()
        if len(sys.argv) > 1:
            if sys.argv[1] == 'debug':
                self.window=uic.loadUi("nokeyfile.ui")
            else:
                self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8')))
                self.setIconWindow()
        else:
            self.window=uic.loadUi(StringIO(base64.b64decode(self.ui).decode('utf-8'))) 
        self.setup_buttons()

        self.window.show()
        self.app.exec()



class licensed:
    nokey=Loader
    loader=None
    keyfile='key.txt'
    def run(self):
        data='''{code}'''

        k=Path(self.keyfile).exists()
        while not k:
            self.loader=self.nokey(keyfile=self.keyfile)
            k=Path(self.keyfile).exists()
            print(k) 
            if self.loader.quitting:
                exit('user does not have a key!')
        try:
            key=bytes()
            with open(self.keyfile,'rb') as xkey:
                key=xkey.read()
            f = Fernet(key)
            decoded = f.decrypt(data.encode())
            exec(decoded,globals())
        except Exception as e:
            with open('loader.log','w') as out:
                out.write(str(e))
            print(e)



    #program=''''''


x=licensed()
x.run()
